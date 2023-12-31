# Generated by Django 4.2.4 on 2023-10-16 20:29

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_appmodel_email_alter_appmodel_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appmodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appmodel',
            name='message',
        ),
        migrations.RemoveField(
            model_name='appmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='appmodel',
            name='subject',
        ),
        migrations.AddField(
            model_name='appmodel',
            name='E-mail',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appmodel',
            name='Message',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appmodel',
            name='Name',
            field=models.CharField(default=datetime.datetime(2023, 10, 16, 20, 29, 25, 160209, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appmodel',
            name='Subject',
            field=models.CharField(default=datetime.datetime(2023, 10, 16, 20, 29, 37, 971665, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
    ]
