# Generated by Django 3.0.2 on 2024-08-01 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0084_auto_20240728_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qualityprofile',
            old_name='quality',
            new_name='profile',
        ),
    ]
