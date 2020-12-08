# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 20:49
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0003_auto_20160628_1721"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeviceBay",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name=b"Name")),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_bays",
                        to="dcim.Device",
                    ),
                ),
                (
                    "installed_device",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parent_bay",
                        to="dcim.Device",
                    ),
                ),
            ],
            options={
                "ordering": ["device", "name"],
            },
        ),
        migrations.CreateModel(
            name="DeviceBayTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
            options={
                "ordering": ["device_type", "name"],
            },
        ),
        migrations.AddField(
            model_name="devicetype",
            name="subdevice_role",
            field=models.NullBooleanField(
                choices=[(None, b"N/A"), (True, b"Parent"), (False, b"Child")],
                default=None,
                help_text=b'Parent devices house child devices in device bays. Select "None" if this device type is neither a parent nor a child.',
                verbose_name=b"Parent/child status",
            ),
        ),
        migrations.AddField(
            model_name="devicebaytemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="device_bay_templates",
                to="dcim.DeviceType",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="devicebaytemplate",
            unique_together=set([("device_type", "name")]),
        ),
        migrations.AlterUniqueTogether(
            name="devicebay",
            unique_together=set([("device", "name")]),
        ),
    ]
