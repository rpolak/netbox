# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 16:28
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0008_reports"),
    ]

    operations = [
        migrations.AddField(
            model_name="topologymap",
            name="type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Network"), (2, "Console"), (3, "Power")], default=1
            ),
        ),
    ]
