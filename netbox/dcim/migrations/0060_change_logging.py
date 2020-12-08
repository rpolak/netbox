# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-13 17:14
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0059_site_latitude_longitude"),
    ]

    operations = [
        migrations.AddField(
            model_name="devicerole",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="devicerole",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="devicetype",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="devicetype",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="platform",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="platform",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="rackgroup",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="rackgroup",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="rackreservation",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="rackrole",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="rackrole",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="region",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="region",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="virtualchassis",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="virtualchassis",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="device",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="device",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="rack",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="rack",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="rackreservation",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="site",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="site",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
