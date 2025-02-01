# Generated by Django 5.1.5 on 2025-01-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_catalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_h2', models.TextField(verbose_name='Заголовок h2')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('swipe_text', models.TextField(verbose_name='Swipe текст')),
                ('img_1', models.FileField(upload_to='budget/', verbose_name='Бюджет 1 изображение')),
                ('title_1', models.TextField(verbose_name='Бюджет 1 заголовок')),
                ('btn_1', models.TextField(verbose_name='Бюджет 1 кнопка')),
                ('img_2', models.FileField(upload_to='budget/', verbose_name='Бюджет 2 изображение')),
                ('title_2', models.TextField(verbose_name='Бюджет 2 заголовок')),
                ('btn_2', models.TextField(verbose_name='Бюджет 2 кнопка')),
                ('img_3', models.FileField(upload_to='budget/', verbose_name='Бюджет 3 изображение')),
                ('title_3', models.TextField(verbose_name='Бюджет 3 заголовок')),
                ('btn_3', models.TextField(verbose_name='Бюджет 3 кнопка')),
                ('img_4', models.FileField(upload_to='budget/', verbose_name='Бюджет 4 изображение')),
                ('title_4', models.TextField(verbose_name='Бюджет 4 заголовок')),
                ('btn_4', models.TextField(verbose_name='Бюджет 4 кнопка')),
            ],
            options={
                'verbose_name': '12 Бюджет',
                'verbose_name_plural': '12 Бюджет',
            },
        ),
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': '11 Каталог', 'verbose_name_plural': '11 Каталог'},
        ),
    ]
