# Generated by Django 2.2.11 on 2020-03-14 06:50

from django.db import migrations, models
import django.db.models.deletion
import extras.utils


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0038_webhook_template_support"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customfield",
            name="obj_type",
            field=models.ManyToManyField(
                limit_choices_to=extras.utils.FeatureQuery("custom_fields"),
                related_name="custom_fields",
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="customlink",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to=extras.utils.FeatureQuery("custom_links"),
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="exporttemplate",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to=extras.utils.FeatureQuery("export_templates"),
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="graph",
            name="type",
            field=models.ForeignKey(
                limit_choices_to=extras.utils.FeatureQuery("graphs"),
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="obj_type",
            field=models.ManyToManyField(
                limit_choices_to=extras.utils.FeatureQuery("webhooks"),
                related_name="webhooks",
                to="contenttypes.ContentType",
            ),
        ),
    ]
