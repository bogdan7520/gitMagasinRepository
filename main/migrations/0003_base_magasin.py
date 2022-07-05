# Generated by Django 4.0.5 on 2022-06-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_magasin_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='base_magasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('photo_1', models.ImageField(blank=True, upload_to='', verbose_name='Фото 1')),
                ('photo_2', models.ImageField(blank=True, upload_to='', verbose_name='Фото 2')),
                ('photo_3', models.ImageField(blank=True, upload_to='', verbose_name='Фото 3')),
                ('photo_4', models.ImageField(blank=True, upload_to='', verbose_name='Фото 4')),
                ('photo_5', models.ImageField(blank=True, upload_to='', verbose_name='Фото 5')),
                ('photo_6', models.ImageField(blank=True, upload_to='', verbose_name='Фото 6')),
                ('photo_7', models.ImageField(blank=True, upload_to='', verbose_name='Фото 7')),
                ('photo_8', models.ImageField(blank=True, upload_to='', verbose_name='Фото 8')),
                ('about', models.TextField(verbose_name='О товаре')),
                ('price', models.CharField(blank=True, max_length=20, verbose_name='Цена')),
                ('tema', models.CharField(max_length=20, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
