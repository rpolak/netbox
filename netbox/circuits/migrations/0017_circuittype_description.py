# Generated by Django 2.2.6 on 2019-12-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("circuits", "0016_3569_circuit_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="circuittype",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
