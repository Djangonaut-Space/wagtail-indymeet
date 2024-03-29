# Generated by Django 4.1.13 on 2024-03-26 14:57
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0023_alter_question_choices_alter_question_type_field_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="help_text",
            field=models.TextField(
                blank=True, help_text="You can add a help text in here."
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="key",
            field=models.CharField(
                blank=True,
                help_text="Unique key for this question, fill in the blank if you want to use for automatic generation.",
                max_length=500,
                unique=True,
            ),
        ),
    ]
