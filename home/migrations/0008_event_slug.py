# Generated by Django 4.1.12 on 2023-10-06 12:29
from django.db import migrations
from django.db import models
from django.utils.text import slugify


def slugify_title(apps, schema_editor):
    Event = apps.get_model("home", "Event")
    for event in Event.objects.filter(slug__isnull=True):
        event.slug = slugify(event.title)
        event.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_eventtag_remove_event_categories_delete_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="slug",
            field=models.SlugField(
                help_text="This is used in the URL to identify the event.", null=True
            ),
        ),
        migrations.RunPython(slugify_title, migrations.RunPython.noop, elidable=True),
    ]
