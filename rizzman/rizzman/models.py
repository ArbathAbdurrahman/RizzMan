from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="risks")
    tujuan = models.TextField()
    proses_bisnis = models.CharField(max_length=255, blank=True, null=True)
    kelompok_resiko = models.CharField(max_length=255, blank=True, null=True)
    kode_resiko = models.CharField(max_length=255, unique=True)  # Unique untuk mencegah duplikasi
    penyebab_resiko = models.TextField()
    sumber_resiko = models.BooleanField()
    akibat = models.TextField()
    akibat_finansial = models.PositiveIntegerField()  # Ubah ke PositiveIntegerField
    pemilik_resiko = models.CharField(max_length=255)
    departemen = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="risks")
    inherent_likelihood = models.PositiveIntegerField()
    inherent_impact = models.PositiveIntegerField()
    inherent_score = models.PositiveIntegerField()
    control = models.BooleanField()
    memadai = models.BooleanField()
    status = models.BooleanField(choices=STATUS_CHOICES, default=True)
    residual_likelihood = models.PositiveIntegerField()
    residual_impact = models.PositiveIntegerField()
    residual_score = models.PositiveIntegerField()
    perlakuan = models.BooleanField()
    tindakan_mitigasi = models.TextField()
    mitigasi_likelihood = models.PositiveIntegerField()
    mitigasi_impact = models.PositiveIntegerField()
    mitigasi_score = models.PositiveIntegerField()
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
    nomor_induk = models.CharField(max_length=50, default=None, null=True)
    jabatan = models.CharField(max_length=100, default=None)
    gelar = models.CharField(max_length=100, blank=True, null=True)
    alamat = models.TextField(default=None)
    tanggal_lahir = models.DateField(default=None)
    foto = models.ImageField(upload_to='user_photos/', blank=True, null=True, default=None)
    total_pengisian = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
