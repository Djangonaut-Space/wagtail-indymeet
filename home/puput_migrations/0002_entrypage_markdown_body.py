# Generated by Django 4.1.13 on 2023-12-11 07:40

from django.db import migrations
import wagtailmarkdown.fields


class Migration(migrations.Migration):
    dependencies = [
        ("puput", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="entrypage",
            name="markdown_body",
            field=wagtailmarkdown.fields.MarkdownField(
                blank=True, null=True, verbose_name="body (Markdown)"
            ),
        ),
    ]
