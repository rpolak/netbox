# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 20:24
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0012_site_rack_device_add_tenant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interface",
            name="form_factor",
            field=models.PositiveSmallIntegerField(
                choices=[
                    [b"Virtual interfaces", [[0, b"Virtual"]]],
                    [
                        b"Ethernet",
                        [
                            [800, b"100BASE-TX (10/100M)"],
                            [1000, b"1000BASE-T (1GE)"],
                            [1150, b"10GBASE-T (10GE)"],
                        ],
                    ],
                    [
                        b"Modular",
                        [
                            [1050, b"GBIC (1GE)"],
                            [1100, b"SFP (1GE)"],
                            [1300, b"XFP (10GE)"],
                            [1200, b"SFP+ (10GE)"],
                            [1400, b"QSFP+ (40GE)"],
                            [1500, b"CFP (100GE)"],
                            [1600, b"QSFP28 (100GE)"],
                        ],
                    ],
                    [
                        b"Serial",
                        [
                            [4000, b"T1 (1.544 Mbps)"],
                            [4010, b"E1 (2.048 Mbps)"],
                            [4040, b"T3 (45 Mbps)"],
                            [4050, b"E3 (34 Mbps)"],
                        ],
                    ],
                    [
                        b"Stacking",
                        [[5000, b"Cisco StackWise"], [5050, b"Cisco StackWise Plus"]],
                    ],
                ],
                default=1200,
            ),
        ),
        migrations.AlterField(
            model_name="interfacetemplate",
            name="form_factor",
            field=models.PositiveSmallIntegerField(
                choices=[
                    [b"Virtual interfaces", [[0, b"Virtual"]]],
                    [
                        b"Ethernet",
                        [
                            [800, b"100BASE-TX (10/100M)"],
                            [1000, b"1000BASE-T (1GE)"],
                            [1150, b"10GBASE-T (10GE)"],
                        ],
                    ],
                    [
                        b"Modular",
                        [
                            [1050, b"GBIC (1GE)"],
                            [1100, b"SFP (1GE)"],
                            [1300, b"XFP (10GE)"],
                            [1200, b"SFP+ (10GE)"],
                            [1400, b"QSFP+ (40GE)"],
                            [1500, b"CFP (100GE)"],
                            [1600, b"QSFP28 (100GE)"],
                        ],
                    ],
                    [
                        b"Serial",
                        [
                            [4000, b"T1 (1.544 Mbps)"],
                            [4010, b"E1 (2.048 Mbps)"],
                            [4040, b"T3 (45 Mbps)"],
                            [4050, b"E3 (34 Mbps)"],
                        ],
                    ],
                    [
                        b"Stacking",
                        [[5000, b"Cisco StackWise"], [5050, b"Cisco StackWise Plus"]],
                    ],
                ],
                default=1200,
            ),
        ),
    ]
