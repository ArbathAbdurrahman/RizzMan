# Generated by Django 4.2 on 2024-12-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rizzman', '0013_alter_risk_perlakuan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='status',
            field=models.BooleanField(choices=[(True, 'Executed'), (False, 'Ongoing')], null=True),
        ),
    ]
