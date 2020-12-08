# Generated by Django 2.0.3 on 2018-03-30 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0010_customfield_filter_logic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customfield",
            name="obj_type",
            field=models.ManyToManyField(
                help_text="The object(s) to which this field applies.",
                limit_choices_to={
                    "model__in": (
                        "provider",
                        "circuit",
                        "site",
                        "rack",
                        "devicetype",
                        "device",
                        "aggregate",
                        "prefix",
                        "ipaddress",
                        "vlan",
                        "vrf",
                        "tenant",
                        "cluster",
                        "virtualmachine",
                    )
                },
                related_name="custom_fields",
                to="contenttypes.ContentType",
                verbose_name="Object(s)",
            ),
        ),
        migrations.AlterField(
            model_name="customfieldchoice",
            name="field",
            field=models.ForeignKey(
                limit_choices_to={"type": 600},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="choices",
                to="extras.CustomField",
            ),
        ),
        migrations.AlterField(
            model_name="exporttemplate",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to={
                    "model__in": [
                        "provider",
                        "circuit",
                        "site",
                        "region",
                        "rack",
                        "rackgroup",
                        "manufacturer",
                        "devicetype",
                        "device",
                        "consoleport",
                        "powerport",
                        "interfaceconnection",
                        "aggregate",
                        "prefix",
                        "ipaddress",
                        "vlan",
                        "tenant",
                        "cluster",
                        "virtualmachine",
                    ]
                },
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.ContentType",
            ),
        ),
    ]
