# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialprice', '0007_auto_20161123_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smm',
            name='pricedate',
            field=models.DateField(max_length=10, verbose_name='行情日期'),
        ),
    ]