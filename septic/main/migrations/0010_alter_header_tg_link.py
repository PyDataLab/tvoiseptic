# Generated by Django 5.1.5 on 2025-01-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_header_messenger_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='tg_link',
            field=models.URLField(verbose_name='Ссылка на телеграм'),
        ),
    ]
