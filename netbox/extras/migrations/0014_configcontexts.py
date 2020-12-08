# Generated by Django 2.0.7 on 2018-07-27 19:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tenancy", "0005_change_logging"),
        ("dcim", "0061_platform_napalm_args"),
        ("extras", "0013_objectchange"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConfigContext",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("weight", models.PositiveSmallIntegerField(default=1000)),
                ("description", models.CharField(blank=True, max_length=100)),
                ("is_active", models.BooleanField(default=True)),
                ("data", django.contrib.postgres.fields.jsonb.JSONField()),
                (
                    "platforms",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_configcontext_platforms_+",
                        to="dcim.Platform",
                    ),
                ),
                (
                    "regions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_configcontext_regions_+",
                        to="dcim.Region",
                    ),
                ),
                (
                    "roles",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_configcontext_roles_+",
                        to="dcim.DeviceRole",
                    ),
                ),
                (
                    "sites",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_configcontext_sites_+",
                        to="dcim.Site",
                    ),
                ),
                (
                    "tenant_groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_configcontext_tenant_groups_+",
                        to="tenancy.TenantGroup",
                    ),
                ),
                (
                    "tenants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_configcontext_tenants_+",
                        to="tenancy.Tenant",
                    ),
                ),
            ],
            options={
                "ordering": ["weight", "name"],
            },
        ),
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
                        "service",
                        "secret",
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
                        "virtualchassis",
                        "aggregate",
                        "prefix",
                        "ipaddress",
                        "vlan",
                        "vrf",
                        "service",
                        "secret",
                        "tenant",
                        "cluster",
                        "virtualmachine",
                    ]
                },
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="obj_type",
            field=models.ManyToManyField(
                help_text="The object(s) to which this Webhook applies.",
                limit_choices_to={
                    "model__in": (
                        "provider",
                        "circuit",
                        "site",
                        "rack",
                        "devicetype",
                        "device",
                        "virtualchassis",
                        "consoleport",
                        "consoleserverport",
                        "powerport",
                        "poweroutlet",
                        "interface",
                        "devicebay",
                        "inventoryitem",
                        "aggregate",
                        "prefix",
                        "ipaddress",
                        "vlan",
                        "vrf",
                        "service",
                        "secret",
                        "tenant",
                        "cluster",
                        "virtualmachine",
                    )
                },
                related_name="webhooks",
                to="contenttypes.ContentType",
                verbose_name="Object types",
            ),
        ),
    ]
