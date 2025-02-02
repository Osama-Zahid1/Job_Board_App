# Generated by Django 5.0.3 on 2024-08-19 07:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerapp', '0011_remove_jobmodel_last_login_remove_jobmodel_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Interview', 'Interview Scheduled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Applied', max_length=50)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekerapp.jobmodel')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
