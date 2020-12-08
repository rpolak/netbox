# Generated by Django 2.0.8 on 2018-09-16 02:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("virtualization", "0007_change_logging"),
    ]

    operations = [
        migrations.AddField(
            model_name="virtualmachine",
            name="local_context_data",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
