# Generated by Django 4.2 on 2024-12-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rizzman', '0017_alter_risk_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='status',
            field=models.CharField(choices=[('Executed', 'Executed'), ('Ongoing', 'Ongoing'), ('Pending', 'Pending')], max_length=50),
        ),
    ]
