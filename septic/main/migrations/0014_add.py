# Generated by Django 5.1.5 on 2025-01-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_maincontent_alter_menu_quiz_link_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_text', models.TextField(verbose_name='Add текст')),
                ('arrow_img', models.FileField(upload_to='add/', verbose_name='Изображение arrow')),
                ('add_text1', models.TextField(verbose_name='Add текст1')),
                ('swipe_img', models.FileField(upload_to='add/', verbose_name='Изображение swipe')),
                ('add1_img', models.FileField(upload_to='add/', verbose_name='Изображение add1')),
                ('add1_title', models.TextField(verbose_name='Add1 title')),
                ('add1_text', models.TextField(verbose_name='Add1 text')),
                ('add2_img', models.FileField(upload_to='add/', verbose_name='Изображение add2')),
                ('add2_title', models.TextField(verbose_name='Add2 title')),
                ('add2_text', models.TextField(verbose_name='Add2 text')),
                ('add3_img', models.FileField(upload_to='add/', verbose_name='Изображение add3')),
                ('add3_title', models.TextField(verbose_name='Add3 title')),
                ('add3_text', models.TextField(verbose_name='Add3 text')),
                ('add5_img', models.FileField(upload_to='add/', verbose_name='Изображение add5')),
                ('add5_title', models.TextField(verbose_name='Add5 title')),
                ('add5_text', models.TextField(verbose_name='Add5 text')),
                ('add6_img', models.FileField(upload_to='add/', verbose_name='Изображение add6')),
                ('add6_title', models.TextField(verbose_name='Add6 title')),
                ('add6_text', models.TextField(verbose_name='Add6 text')),
            ],
            options={
                'verbose_name': '06_Add',
                'verbose_name_plural': '06_Add',
            },
        ),
    ]
