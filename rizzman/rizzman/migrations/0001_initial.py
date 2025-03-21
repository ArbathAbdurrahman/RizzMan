# Generated by Django 4.2.5 on 2024-11-21 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_induk', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=100)),
                ('gelar', models.CharField(blank=True, max_length=100, null=True)),
                ('alamat', models.TextField()),
                ('tanggal_lahir', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='user_photos/')),
                ('total_pengisian', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tujuan', models.TextField()),
                ('proses_bisnis', models.CharField(max_length=255)),
                ('kelompok_resiko', models.CharField(max_length=255)),
                ('kode_resiko', models.CharField(max_length=255)),
                ('penyebab_resiko', models.TextField()),
                ('sumber_resiko', models.BooleanField()),
                ('akibat', models.TextField()),
                ('akibat_finansial', models.IntegerField()),
                ('pemilik_resiko', models.CharField(max_length=255)),
                ('departemen', models.CharField(max_length=255)),
                ('inherent_likelihood', models.IntegerField()),
                ('inherent_impact', models.IntegerField()),
                ('inherent_score', models.IntegerField()),
                ('control', models.BooleanField()),
                ('memadai', models.BooleanField()),
                ('status', models.BooleanField()),
                ('residual_likelihood', models.IntegerField()),
                ('residual_impact', models.IntegerField()),
                ('residual_score', models.IntegerField()),
                ('perlakuan', models.BooleanField()),
                ('tindakan_mitigasi', models.TextField()),
                ('mitigasi_likelihood', models.IntegerField()),
                ('mitigasi_impact', models.IntegerField()),
                ('mitigasi_score', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('total_modifikasi', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
