# Generated by Django 5.0.3 on 2024-06-23 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seekerapp', '0010_rename_active_recruitermodel_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='jobmodel',
            name='password',
        ),
    ]
