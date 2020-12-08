# Generated by Django 3.0.3 on 2020-03-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0040_standardize_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="comments",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.RenameField(
            model_name="tag",
            old_name="comments",
            new_name="description",
        ),
    ]
