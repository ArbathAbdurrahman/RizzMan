from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
import os

class Department(models.Model):
    """Model untuk departemen."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Bisnis(models.Model):
    """Model untuk Bisnis."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Kelompok(models.Model):
    """Model untuk kelompok resiko."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Risk(models.Model):
    """Model untuk risiko."""
    STATUS_CHOICES = [
        (True, 'Executed'),
        (False, 'Ongoing'),
    ]
    SUMBER_RESIKO_CHOICES = [
    ('internal', 'Internal'),
    ('external', 'External'),
    ('both', 'Internal dan External'),
    ]
    MEMADAI_CHOICES = [
        (True, 'Memadai'),
        (False, 'Tidak Memadai'),
    ]
    STATUS_CONTROL = [
        (True, 'Ada'),
        (False, 'Tidak'),
    ]
    STATUS_PERLAKUAN = [
        (True, 'Accept'),
        (True, 'Reduce'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="risks")
    tujuan = models.TextField()
    proses_bisnis = models.ForeignKey(Bisnis, on_delete=models.SET_NULL, null=True, related_name="risks")
    kelompok_resiko = models.ForeignKey(Kelompok, on_delete=models.SET_NULL, null=True, related_name="risks")
    kode_resiko = models.CharField(max_length=255, unique=True)  # Tidak boleh null
    uraian_peristiwa = models.TextField()
    penyebab_resiko = models.TextField()
    sumber_resiko = models.CharField(max_length=100,choices=SUMBER_RESIKO_CHOICES)
    akibat = models.TextField()
    akibat_finansial = models.PositiveIntegerField()  # Tidak boleh negatif
    pemilik_resiko = models.CharField(max_length=255)
    departemen = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="risks")
    inherent_likelihood = models.PositiveIntegerField(default=0)
    inherent_impact = models.PositiveIntegerField(default=0)
    inherent_score = models.PositiveIntegerField(default=0)
    control = models.BooleanField(choices=STATUS_CONTROL)
    memadai = models.BooleanField(choices=MEMADAI_CHOICES)
    status = models.BooleanField(choices=STATUS_CHOICES)
    residual_likelihood = models.PositiveIntegerField(default=0)
    residual_impact = models.PositiveIntegerField(default=0)
    residual_score = models.PositiveIntegerField(default=0)
    perlakuan = models.BooleanField(choices=STATUS_PERLAKUAN)
    tindakan_mitigasi = models.TextField()
    mitigasi_likelihood = models.PositiveIntegerField(default=0)
    mitigasi_impact = models.PositiveIntegerField(default=0)
    mitigasi_score = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    total_modifikasi = models.PositiveIntegerField(default=0)
    tingkat = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Risk {self.kode_resiko} - {self.tujuan}"

    def clean(self):
        """Validasi tambahan untuk data."""
        if self.inherent_score < 0 or self.residual_score < 0 or self.mitigasi_score < 0:
            raise ValidationError("Score values cannot be negative.")

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    priority = models.IntegerField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    """Profil tambahan untuk pengguna."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nama = models.CharField(max_length=50, blank=True, null=True)
    jabatan = models.ForeignKey(Role,max_length=100, blank=True, null=True, on_delete=models.SET_NULL,default=None)
    alamat = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='user_photos/', blank=True, null=True, default='herta.jpg')
    total_pengisian = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Penambahan tingkat otomatis
@receiver(pre_save, sender=Risk)
def set_risk_level(sender, instance, **kwargs):
    try:
        if instance.user and hasattr(instance.user, 'profile') and instance.user.profile and instance.user.profile.jabatan:
            instance.tingkat = instance.user.profile.jabatan.priority
        else:
            instance.tingkat = None
    except Exception as e:
        # Log error atau set tingkat ke default
        instance.tingkat = None

# Signals untuk mendeteksi penghapusan foto profil
@receiver(post_delete, sender=UserProfile)
def delete_profile_photo_on_delete(sender, instance, **kwargs):
    """Hapus file foto profil saat UserProfile dihapus."""
    if instance.foto and instance.foto.name != 'herta.jpg':  # Pastikan default foto tidak dihapus
        if os.path.isfile(instance.foto.path):
            try:
                os.remove(instance.foto.path)
            except Exception as e:
                print(f"Error saat menghapus foto: {e}")

@receiver(pre_save, sender=UserProfile)
def delete_old_profile_photo_on_update(sender, instance, **kwargs):
    """Hapus file foto lama saat diperbarui dengan foto baru."""
    if not instance.pk:  # Jika instance baru, abaikan
        return

    try:
        old_instance = UserProfile.objects.get(pk=instance.pk)
    except UserProfile.DoesNotExist:
        return

    # Jika foto diubah, hapus foto lama
    if old_instance.foto != instance.foto and old_instance.foto.name != 'herta.jpg':
        if old_instance.foto and os.path.isfile(old_instance.foto.path):
            try:
                os.remove(old_instance.foto.path)
            except Exception as e:
                print(f"Error saat menghapus foto lama: {e}")

# Signal untuk membuat profil pengguna saat user baru dibuat
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signal untuk membuat profil pengguna ketika user baru dibuat."""
    if created:
        UserProfile.objects.create(user=instance)


# Signal untuk menyimpan profil pengguna saat user diperbarui
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Signal untuk menyimpan profil pengguna ketika user diperbarui."""
    if hasattr(instance, 'profile'):
        instance.profile.save()
