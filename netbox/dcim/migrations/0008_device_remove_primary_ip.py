# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 19:01
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0007_device_copy_primary_ip"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="device",
            name="primary_ip",
        ),
    ]
