# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-25 22:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180225_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='days_remaining',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='licence_type',
        ),
        migrations.AlterField(
            model_name='notification',
            name='truck_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Truck'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
