# Generated by Django 4.2.4 on 2024-05-23 05:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_contact_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time_job',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=255, null=True, verbose_name='Время и график работы'),
        ),
    ]
