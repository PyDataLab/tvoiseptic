# Generated by Django 5.1.5 on 2025-02-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_popupstock'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopupPolitic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(verbose_name='Текст полностью')),
            ],
            options={
                'verbose_name': '27 Всплывающее окно политика',
                'verbose_name_plural': '27 Всплывающее окно политика',
            },
        ),
    ]
