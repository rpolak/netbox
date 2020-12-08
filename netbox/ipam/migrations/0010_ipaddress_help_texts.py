# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 17:46
from django.db import migrations, models
import django.db.models.deletion
import ipam.fields


class Migration(migrations.Migration):

    dependencies = [
        ("ipam", "0009_ipaddress_add_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ipaddress",
            name="address",
            field=ipam.fields.IPAddressField(
                help_text=b"IPv4 or IPv6 address (with mask)"
            ),
        ),
        migrations.AlterField(
            model_name="ipaddress",
            name="nat_inside",
            field=models.OneToOneField(
                blank=True,
                help_text=b'The IP for which this address is the "outside" IP',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="nat_outside",
                to="ipam.IPAddress",
                verbose_name=b"NAT (Inside)",
            ),
        ),
    ]
