# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_auto_20160916_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsinstrukciy',
            name='file',
            field=models.FileField(upload_to='docs/', verbose_name='Файл для скачування'),
        ),
    ]
