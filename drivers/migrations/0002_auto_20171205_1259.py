# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 09:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RenameField(
            model_name='cardetails',
            old_name='model',
            new_name='car_model',
        ),
        migrations.RenameField(
            model_name='driverprofile',
            old_name='driver',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='driverprofile',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='driverprofile',
            name='destination',
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='email',
            field=models.EmailField(default=datetime.datetime(2017, 12, 5, 9, 59, 18, 988980, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='driverphotos/'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]