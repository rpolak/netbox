# Generated by Django 2.1.4 on 2019-02-20 06:56

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0069_deprecate_nullablecharfield"),
        ("extras", "0019_tag_taggeditem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consoleport",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="consoleserverport",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="devicebay",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="devicetype",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="frontport",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="interface",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="poweroutlet",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="powerport",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="rack",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="rearport",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="virtualchassis",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
    ]
