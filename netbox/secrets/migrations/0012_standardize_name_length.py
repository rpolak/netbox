# Generated by Django 3.1 on 2020-10-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("secrets", "0011_secret_generic_assignments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secretrole",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="secretrole",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
