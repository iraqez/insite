# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Файл для скачування')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документи',
            },
        ),
        migrations.CreateModel(
            name='Leading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Унікальне значення в адресній строці, добавляється автоматично.', max_length=255, unique=True, verbose_name='Адресна строка')),
                ('title', models.CharField(max_length=100, verbose_name='Назва процедури')),
                ('text', tinymce.models.HTMLField(verbose_name='Зміст процедури')),
            ],
            options={
                'verbose_name': 'Процедура',
                'verbose_name_plural': 'Процедури',
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва підрозділу')),
                ('slug', models.SlugField(help_text='Унікальне значення в адресній строці, добавляється автоматично.', max_length=255, unique=True, verbose_name='Адресна строка')),
            ],
            options={
                'verbose_name': 'Підрозділ',
                'verbose_name_plural': 'Підрозділи',
            },
        ),
        migrations.AddField(
            model_name='leading',
            name='subdivision',
            field=models.ManyToManyField(to='instr.Subdivision', verbose_name='Підрозділ'),
        ),
        migrations.AddField(
            model_name='docs',
            name='leading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instr.Leading'),
        ),
    ]
