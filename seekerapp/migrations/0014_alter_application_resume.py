# Generated by Django 5.0.3 on 2024-08-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerapp', '0013_jobmodel_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='resume/'),
        ),
    ]
