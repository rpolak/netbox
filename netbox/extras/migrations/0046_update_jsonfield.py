# Generated by Django 3.1b1 on 2020-07-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0045_configcontext_changelog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="configcontext",
            name="data",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="jobresult",
            name="data",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="objectchange",
            name="object_data",
            field=models.JSONField(editable=False),
        ),
    ]
