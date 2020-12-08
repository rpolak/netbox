# Generated by Django 2.1.7 on 2019-02-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0070_custom_tag_models"),
    ]

    operations = [
        migrations.AddField(
            model_name="consoleport",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="devicebay",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="powerport",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
