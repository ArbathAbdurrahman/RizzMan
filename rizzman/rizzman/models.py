from django.contrib.auth.models import User
from django.db import models


class Risk(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="risks")
    user = models.TextField()
    tujuan = models.TextField()
    proses_bisnis = models.CharField(max_length=255)
    kelompok_resiko = models.CharField(max_length=255)
    kode_resiko = models.CharField(max_length=255)
    penyebab_resiko = models.TextField()
    sumber_resiko = models.BooleanField()
    akibat = models.TextField()
    akibat_finansial = models.IntegerField()
    pemilik_resiko = models.CharField(max_length=255)
    departemen = models.CharField(max_length=255)
    inherent_likelihood = models.IntegerField()
    inherent_impact = models.IntegerField()
    inherent_score = models.IntegerField()
    control = models.BooleanField()
    memadai = models.BooleanField()
    status = models.BooleanField()
    residual_likelihood = models.IntegerField()
    residual_impact = models.IntegerField()
    residual_score = models.IntegerField()
    perlakuan = models.BooleanField()
    tindakan_mitigasi = models.TextField()
    mitigasi_likelihood = models.IntegerField()
    mitigasi_impact = models.IntegerField()
    mitigasi_score = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    total_modifikasi = models.IntegerField(default=0)
    kode_resiko = models.CharField(max_length=255)

    def __str__(self):
        return f"Risk {self.kode_resiko} - {self.tujuan}"

class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user = models.TextField()
    password = models.TextField()
    namalengkap= models.CharField(max_length=300,null=True,blank=True,default='Unknown')
    nomor_induk = models.CharField(max_length=50,default=None,null=True)
    jabatan = models.CharField(max_length=100,default=None)
    gelar = models.CharField(max_length=100, blank=True,null=True,default="Unknown")
    alamat = models.TextField(default=None)
    tanggal_lahir = models.DateField(default=None)
    foto = models.ImageField(upload_to='user_photos/', blank=True, null=True,default="user_photos/herta.jpg")
    total_pengisian = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
