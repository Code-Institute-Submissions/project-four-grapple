# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-16 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product', max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('summary', models.TextField(max_length=200, verbose_name='Summary')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=9.99, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
