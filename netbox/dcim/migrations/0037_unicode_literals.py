# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 15:34
import dcim.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utilities.fields


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0036_add_ff_juniper_vcp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consoleport",
            name="connection_status",
            field=models.NullBooleanField(
                choices=[[False, "Planned"], [True, "Connected"]], default=True
            ),
        ),
        migrations.AlterField(
            model_name="consoleport",
            name="cs_port",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="connected_console",
                to="dcim.ConsoleServerPort",
                verbose_name="Console server port",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="asset_tag",
            field=utilities.fields.NullableCharField(
                blank=True,
                help_text="A unique tag used to identify this device",
                max_length=50,
                null=True,
                unique=True,
                verbose_name="Asset tag",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="face",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[[0, "Front"], [1, "Rear"]],
                null=True,
                verbose_name="Rack face",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="position",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="The lowest-numbered unit occupied by the device",
                null=True,
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Position (U)",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="primary_ip4",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_ip4_for",
                to="ipam.IPAddress",
                verbose_name="Primary IPv4",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="primary_ip6",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_ip6_for",
                to="ipam.IPAddress",
                verbose_name="Primary IPv6",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="serial",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Serial number"
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    [1, "Active"],
                    [0, "Offline"],
                    [2, "Planned"],
                    [3, "Staged"],
                    [4, "Failed"],
                    [5, "Inventory"],
                ],
                default=1,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="devicebay",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="interface_ordering",
            field=models.PositiveSmallIntegerField(
                choices=[[1, "Slot/position"], [2, "Name (alphabetically)"]], default=1
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="is_console_server",
            field=models.BooleanField(
                default=False,
                help_text="This type of device has console server ports",
                verbose_name="Is a console server",
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="is_full_depth",
            field=models.BooleanField(
                default=True,
                help_text="Device consumes both front and rear rack faces",
                verbose_name="Is full depth",
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="is_network_device",
            field=models.BooleanField(
                default=True,
                help_text="This type of device has network interfaces",
                verbose_name="Is a network device",
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="is_pdu",
            field=models.BooleanField(
                default=False,
                help_text="This type of device has power outlets",
                verbose_name="Is a PDU",
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="part_number",
            field=models.CharField(
                blank=True, help_text="Discrete part number (optional)", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="subdevice_role",
            field=models.NullBooleanField(
                choices=[(None, "None"), (True, "Parent"), (False, "Child")],
                default=None,
                help_text='Parent devices house child devices in device bays. Select "None" if this device type is neither a parent nor a child.',
                verbose_name="Parent/child status",
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="u_height",
            field=models.PositiveSmallIntegerField(
                default=1, verbose_name="Height (U)"
            ),
        ),
        migrations.AlterField(
            model_name="interface",
            name="form_factor",
            field=models.PositiveSmallIntegerField(
                choices=[
                    [
                        "Virtual interfaces",
                        [[0, "Virtual"], [200, "Link Aggregation Group (LAG)"]],
                    ],
                    [
                        "Ethernet (fixed)",
                        [
                            [800, "100BASE-TX (10/100ME)"],
                            [1000, "1000BASE-T (1GE)"],
                            [1150, "10GBASE-T (10GE)"],
                        ],
                    ],
                    [
                        "Ethernet (modular)",
                        [
                            [1050, "GBIC (1GE)"],
                            [1100, "SFP (1GE)"],
                            [1200, "SFP+ (10GE)"],
                            [1300, "XFP (10GE)"],
                            [1310, "XENPAK (10GE)"],
                            [1320, "X2 (10GE)"],
                            [1350, "SFP28 (25GE)"],
                            [1400, "QSFP+ (40GE)"],
                            [1500, "CFP (100GE)"],
                            [1600, "QSFP28 (100GE)"],
                        ],
                    ],
                    [
                        "FibreChannel",
                        [
                            [3010, "SFP (1GFC)"],
                            [3020, "SFP (2GFC)"],
                            [3040, "SFP (4GFC)"],
                            [3080, "SFP+ (8GFC)"],
                            [3160, "SFP+ (16GFC)"],
                        ],
                    ],
                    [
                        "Serial",
                        [
                            [4000, "T1 (1.544 Mbps)"],
                            [4010, "E1 (2.048 Mbps)"],
                            [4040, "T3 (45 Mbps)"],
                            [4050, "E3 (34 Mbps)"],
                            [4050, "E3 (34 Mbps)"],
                        ],
                    ],
                    [
                        "Stacking",
                        [
                            [5000, "Cisco StackWise"],
                            [5050, "Cisco StackWise Plus"],
                            [5100, "Cisco FlexStack"],
                            [5150, "Cisco FlexStack Plus"],
                            [5200, "Juniper VCP"],
                        ],
                    ],
                    ["Other", [[32767, "Other"]]],
                ],
                default=1200,
            ),
        ),
        migrations.AlterField(
            model_name="interface",
            name="lag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="member_interfaces",
                to="dcim.Interface",
                verbose_name="Parent LAG",
            ),
        ),
        migrations.AlterField(
            model_name="interface",
            name="mac_address",
            field=dcim.fields.MACAddressField(
                blank=True, null=True, verbose_name="MAC Address"
            ),
        ),
        migrations.AlterField(
            model_name="interface",
            name="mgmt_only",
            field=models.BooleanField(
                default=False,
                help_text="This interface is used only for out-of-band management",
                verbose_name="OOB Management",
            ),
        ),
        migrations.AlterField(
            model_name="interfaceconnection",
            name="connection_status",
            field=models.BooleanField(
                choices=[[False, "Planned"], [True, "Connected"]],
                default=True,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="interfacetemplate",
            name="form_factor",
            field=models.PositiveSmallIntegerField(
                choices=[
                    [
                        "Virtual interfaces",
                        [[0, "Virtual"], [200, "Link Aggregation Group (LAG)"]],
                    ],
                    [
                        "Ethernet (fixed)",
                        [
                            [800, "100BASE-TX (10/100ME)"],
                            [1000, "1000BASE-T (1GE)"],
                            [1150, "10GBASE-T (10GE)"],
                        ],
                    ],
                    [
                        "Ethernet (modular)",
                        [
                            [1050, "GBIC (1GE)"],
                            [1100, "SFP (1GE)"],
                            [1200, "SFP+ (10GE)"],
                            [1300, "XFP (10GE)"],
                            [1310, "XENPAK (10GE)"],
                            [1320, "X2 (10GE)"],
                            [1350, "SFP28 (25GE)"],
                            [1400, "QSFP+ (40GE)"],
                            [1500, "CFP (100GE)"],
                            [1600, "QSFP28 (100GE)"],
                        ],
                    ],
                    [
                        "FibreChannel",
                        [
                            [3010, "SFP (1GFC)"],
                            [3020, "SFP (2GFC)"],
                            [3040, "SFP (4GFC)"],
                            [3080, "SFP+ (8GFC)"],
                            [3160, "SFP+ (16GFC)"],
                        ],
                    ],
                    [
                        "Serial",
                        [
                            [4000, "T1 (1.544 Mbps)"],
                            [4010, "E1 (2.048 Mbps)"],
                            [4040, "T3 (45 Mbps)"],
                            [4050, "E3 (34 Mbps)"],
                            [4050, "E3 (34 Mbps)"],
                        ],
                    ],
                    [
                        "Stacking",
                        [
                            [5000, "Cisco StackWise"],
                            [5050, "Cisco StackWise Plus"],
                            [5100, "Cisco FlexStack"],
                            [5150, "Cisco FlexStack Plus"],
                            [5200, "Juniper VCP"],
                        ],
                    ],
                    ["Other", [[32767, "Other"]]],
                ],
                default=1200,
            ),
        ),
        migrations.AlterField(
            model_name="interfacetemplate",
            name="mgmt_only",
            field=models.BooleanField(default=False, verbose_name="Management only"),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="discovered",
            field=models.BooleanField(default=False, verbose_name="Discovered"),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="part_id",
            field=models.CharField(blank=True, max_length=50, verbose_name="Part ID"),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="serial",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Serial number"
            ),
        ),
        migrations.AlterField(
            model_name="platform",
            name="rpc_client",
            field=models.CharField(
                blank=True,
                choices=[
                    ["juniper-junos", "Juniper Junos (NETCONF)"],
                    ["cisco-ios", "Cisco IOS (SSH)"],
                    ["opengear", "Opengear (SSH)"],
                ],
                max_length=30,
                verbose_name="RPC client",
            ),
        ),
        migrations.AlterField(
            model_name="powerport",
            name="connection_status",
            field=models.NullBooleanField(
                choices=[[False, "Planned"], [True, "Connected"]], default=True
            ),
        ),
        migrations.AlterField(
            model_name="rack",
            name="desc_units",
            field=models.BooleanField(
                default=False,
                help_text="Units are numbered top-to-bottom",
                verbose_name="Descending units",
            ),
        ),
        migrations.AlterField(
            model_name="rack",
            name="facility_id",
            field=utilities.fields.NullableCharField(
                blank=True, max_length=30, null=True, verbose_name="Facility ID"
            ),
        ),
        migrations.AlterField(
            model_name="rack",
            name="type",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (100, "2-post frame"),
                    (200, "4-post frame"),
                    (300, "4-post cabinet"),
                    (1000, "Wall-mounted frame"),
                    (1100, "Wall-mounted cabinet"),
                ],
                null=True,
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="rack",
            name="u_height",
            field=models.PositiveSmallIntegerField(
                default=42,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="Height (U)",
            ),
        ),
        migrations.AlterField(
            model_name="rack",
            name="width",
            field=models.PositiveSmallIntegerField(
                choices=[(19, "19 inches"), (23, "23 inches")],
                default=19,
                help_text="Rail-to-rail width",
                verbose_name="Width",
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="asn",
            field=dcim.fields.ASNField(blank=True, null=True, verbose_name="ASN"),
        ),
        migrations.AlterField(
            model_name="site",
            name="contact_email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Contact E-mail"
            ),
        ),
    ]
