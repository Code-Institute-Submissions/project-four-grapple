# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-16 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Product', max_length=150),
        ),
    ]
