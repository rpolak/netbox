# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 18:39
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0032_device_increase_name_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rackreservation",
            name="rack",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="dcim.Rack",
            ),
        ),
    ]
