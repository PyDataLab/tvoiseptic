# Generated by Django 5.1.5 on 2025-01-30 05:19

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_header_messenger_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='messenger_text',
            field=tinymce.models.HTMLField(verbose_name='Текст для мессенджеров'),
        ),
    ]
