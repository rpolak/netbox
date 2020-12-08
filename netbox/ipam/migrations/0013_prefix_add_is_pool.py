# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 19:34
from django.db import migrations, models
import django.db.models.deletion
import ipam.fields


class Migration(migrations.Migration):

    dependencies = [
        ("ipam", "0012_services"),
    ]

    operations = [
        migrations.AddField(
            model_name="prefix",
            name="is_pool",
            field=models.BooleanField(
                default=False,
                help_text=b"All IP addresses within this prefix are considered usable",
                verbose_name=b"Is a pool",
            ),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="prefix",
            field=ipam.fields.IPNetworkField(
                help_text=b"IPv4 or IPv6 network with mask"
            ),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="role",
            field=models.ForeignKey(
                blank=True,
                help_text=b"The primary function of this prefix",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="prefixes",
                to="ipam.Role",
            ),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, b"Container"),
                    (1, b"Active"),
                    (2, b"Reserved"),
                    (3, b"Deprecated"),
                ],
                default=1,
                help_text=b"Operational status of this prefix",
                verbose_name=b"Status",
            ),
        ),
    ]
