# Generated by Django 5.0.3 on 2024-03-09 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('seekerapp', '0002_alter_usermodel_options_alter_usermodel_groups_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usermodel',
            new_name='Seekermodel',
        ),
    ]
