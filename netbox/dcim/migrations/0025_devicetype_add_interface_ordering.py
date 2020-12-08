# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 16:56
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0024_site_add_contact_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="devicetype",
            name="interface_ordering",
            field=models.PositiveSmallIntegerField(
                choices=[[1, b"Slot/position"], [2, b"Name (alphabetically)"]],
                default=1,
            ),
        ),
    ]
