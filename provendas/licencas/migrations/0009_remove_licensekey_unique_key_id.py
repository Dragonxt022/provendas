# Generated by Django 5.1.2 on 2024-11-14 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licencas', '0008_remove_licensekey_system_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licensekey',
            name='unique_key_id',
        ),
    ]