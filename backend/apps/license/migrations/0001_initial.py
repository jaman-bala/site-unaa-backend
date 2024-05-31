# Generated by Django 4.2.4 on 2024-05-27 10:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(blank=True, max_length=599, verbose_name='Наименование на русском')),
                ('title_kg', models.CharField(blank=True, max_length=599, verbose_name='Наименование на кыргызском')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Статья на русском')),
                ('text_ky', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Статья на кыргызском')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Перечень',
                'verbose_name_plural': 'Перечни',
            },
        ),
        migrations.CreateModel(
            name='DocumentsNPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(blank=True, max_length=599, verbose_name='Наименование на русском')),
                ('title_kg', models.CharField(blank=True, max_length=599, verbose_name='Наименование на кыргызском')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Статья на русском')),
                ('text_ky', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Статья на кыргызском')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'НПА',
                'verbose_name_plural': 'НПА',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='license/logo', verbose_name='Логотип')),
                ('title_ru', models.CharField(blank=True, max_length=599, verbose_name='Наименование на русском')),
                ('title_kg', models.CharField(blank=True, max_length=599, verbose_name='Наименование на кыргызском')),
                ('register_number', models.CharField(blank=True, max_length=599, verbose_name='Регистрационный номер')),
                ('address_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=599, verbose_name='Адрес на русском')),
                ('address_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=599, verbose_name='Адрес на кыргызском')),
                ('category', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=599, verbose_name='Категория')),
                ('issued_authority_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=599, verbose_name='Выданный орган на русском')),
                ('issued_authority_kg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=599, verbose_name='Выданный орган на кыргызском')),
                ('date', models.DateTimeField(verbose_name='Дата выдачи')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лизензии для автошкол',
            },
        ),

    ]