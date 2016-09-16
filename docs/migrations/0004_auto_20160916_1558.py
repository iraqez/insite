# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_auto_20160916_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsinstrukciy',
            name='file',
            field=models.FileField(upload_to='docs/Insrtukciy/', verbose_name='Файл для скачування'),
        ),
        migrations.AlterField(
            model_name='docspolozhennya',
            name='file',
            field=models.FileField(upload_to='docs/Polozhennya/', verbose_name='Файл для скачування'),
        ),
        migrations.AlterField(
            model_name='docsprocedure',
            name='file',
            field=models.FileField(upload_to='docs/Procedure/', verbose_name='Файл для скачування'),
        ),
    ]
