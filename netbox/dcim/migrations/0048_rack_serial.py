# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 18:50
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0047_more_100ge_form_factors"),
    ]

    operations = [
        migrations.AddField(
            model_name="rack",
            name="serial",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Serial number"
            ),
        ),
    ]
