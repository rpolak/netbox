# Generated by Django 2.2.6 on 2019-12-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0086_device_name_nonunique"),
    ]

    operations = [
        migrations.AddField(
            model_name="devicerole",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="rackrole",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
