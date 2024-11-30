from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver


class Department(models.Model):
    """Model untuk departemen."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Risk(models.Model):
    """Model untuk risiko."""
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="risks")
    tujuan = models.TextField()
    proses_bisnis = models.CharField(max_length=255, blank=True, null=True)
    kelompok_resiko = models.CharField(max_length=255, blank=True, null=True)
    kode_resiko = models.CharField(max_length=255, unique=True)  # Tidak boleh null
    penyebab_resiko = models.TextField()
    sumber_resiko = models.CharField(max_length=10,choices=SUMBER_RESIKO_CHOICES,default='both'),
    akibat = models.TextField()
    akibat_finansial = models.PositiveIntegerField()  # Tidak boleh negatif
    pemilik_resiko = models.CharField(max_length=255)
    departemen = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="risks")
    inherent_likelihood = models.PositiveIntegerField(default=0)
    inherent_impact = models.PositiveIntegerField(default=0)
    inherent_score = models.PositiveIntegerField(default=0)
    control = models.BooleanField()
    memadai = models.BooleanField(choices=MEMADAI_CHOICES)
    status = models.BooleanField(choices=STATUS_CHOICES, default=True)
    residual_likelihood = models.PositiveIntegerField(default=0)
    residual_impact = models.PositiveIntegerField(default=0)
    residual_score = models.PositiveIntegerField(default=0)
    perlakuan = models.BooleanField()
    tindakan_mitigasi = models.TextField()
    mitigasi_likelihood = models.PositiveIntegerField(default=0)
    mitigasi_impact = models.PositiveIntegerField(default=0)
    mitigasi_score = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    total_modifikasi = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Risk {self.kode_resiko} - {self.tujuan}"

    def clean(self):
        """Validasi tambahan untuk data."""
        if self.inherent_score < 0 or self.residual_score < 0 or self.mitigasi_score < 0:
            raise ValidationError("Score values cannot be negative.")

        if self.residual_score > self.inherent_score:
            raise ValidationError("Residual score cannot be higher than inherent score.")


class UserProfile(models.Model):
    """Profil tambahan untuk pengguna."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nomor_induk = models.CharField(max_length=50, blank=True, null=True)
    jabatan = models.CharField(max_length=100, blank=True, null=True)
    gelar = models.CharField(max_length=100, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    total_pengisian = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"


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
