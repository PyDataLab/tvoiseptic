# Generated by Django 5.1.5 on 2025-01-31 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_guarantees'),
    ]

    operations = [
        migrations.CreateModel(
            name='More',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(verbose_name='Текст 1')),
                ('block1_title', models.TextField(verbose_name='Блок 1 заголовок')),
                ('block1_text', models.TextField(verbose_name='Блок 1 текст')),
                ('block2_title', models.TextField(verbose_name='Блок 2 заголовок')),
                ('block2_text', models.TextField(verbose_name='Блок 2 текст')),
                ('block3_title', models.TextField(verbose_name='Блок 3 заголовок')),
                ('block3_text', models.TextField(verbose_name='Блок 3 текст')),
                ('block4_title', models.TextField(verbose_name='Блок 4 заголовок')),
                ('block4_text', models.TextField(verbose_name='Блок 4 текст')),
                ('block5_title', models.TextField(verbose_name='Блок 5 заголовок')),
                ('block5_text', models.TextField(verbose_name='Блок 5 текст')),
                ('block6_title', models.TextField(verbose_name='Блок 6 заголовок')),
                ('block6_text', models.TextField(verbose_name='Блок 6 текст')),
                ('footer_img', models.FileField(upload_to='more/', verbose_name='Футер изображение')),
                ('footer_text', models.TextField(verbose_name='Футер текст')),
            ],
            options={
                'verbose_name': '14 Подробнее',
                'verbose_name_plural': '14 Подробнее',
            },
        ),
    ]
