# Generated by Django 4.1.13 on 2024-01-23 01:46
from __future__ import annotations

import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_alter_event_organizers_alter_event_rsvped_members_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generalpage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("text-5xl", "h1"),
                                            ("text-4xl", "h2"),
                                            ("text-3xl", "h3"),
                                            ("text-2xl", "h4"),
                                            ("text-xl", "h5"),
                                            ("text-lg", "h6"),
                                        ],
                                        icon="title",
                                    ),
                                ),
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(
                                        class_name="heading-blog", max_length=255
                                    ),
                                ),
                            ],
                            class_name="full",
                        ),
                    ),
                    ("subheading", wagtail.blocks.CharBlock(class_name="full")),
                    ("paragraph", wagtail.blocks.RichTextBlock(class_name="full")),
                    ("HTML", wagtail.blocks.RawHTMLBlock(class_name="full")),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "text_with_heading",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("text-5xl", "h1"),
                                            ("text-4xl", "h2"),
                                            ("text-3xl", "h3"),
                                            ("text-2xl", "h4"),
                                            ("text-xl", "h5"),
                                            ("text-lg", "h6"),
                                        ],
                                        icon="title",
                                    ),
                                ),
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(
                                        class_name="heading-blog", max_length=255
                                    ),
                                ),
                            ],
                            class_name="full",
                        ),
                    ),
                    (
                        "text_heading_image",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(max_length=255)),
                                ("text", wagtail.blocks.TextBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ],
                            class_name="full",
                        ),
                    ),
                    (
                        "video_embed",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(max_length=255)),
                                ("text", wagtail.blocks.TextBlock()),
                            ],
                            class_name="full",
                        ),
                    ),
                    (
                        "table",
                        wagtail.contrib.table_block.blocks.TableBlock(
                            class_name="full"
                        ),
                    ),
                    (
                        "code_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("Python", "python"),
                                            ("Markup", "html"),
                                            ("CSS", "css"),
                                            ("Clojure", "clojure"),
                                            ("Bash", "shell"),
                                            ("Django", "django"),
                                            ("Jinja2", "jinja2"),
                                            ("Docker", "dockerfile"),
                                            ("Git", "git"),
                                            ("GraphQL", "graphql"),
                                            ("Handlebars", "handlebars"),
                                            (".ignore", "gitignore"),
                                            ("JSON", "json"),
                                            ("JSON5", "json5"),
                                            ("Markdown", "md"),
                                            ("Markdown", "md"),
                                            ("React JSX", "jsx"),
                                            ("React TSX", "tsx"),
                                            ("SASS", "sass"),
                                            ("SCSS", "scss"),
                                            ("TypeScript", "ts"),
                                            ("vim", "vim"),
                                        ]
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.blocks.CharBlock(
                                        blank=True, max_length=255
                                    ),
                                ),
                                (
                                    "page",
                                    wagtail.blocks.CharBlock(
                                        blank=True, max_length=255
                                    ),
                                ),
                                (
                                    "code",
                                    wagtail.blocks.TextBlock(
                                        blank=True, max_length=1000
                                    ),
                                ),
                            ],
                            class_name="full",
                        ),
                    ),
                    (
                        "quote_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.CharBlock(max_length=255)),
                                (
                                    "attribution",
                                    wagtail.blocks.CharBlock(max_length=255),
                                ),
                            ],
                            class_name="full",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
