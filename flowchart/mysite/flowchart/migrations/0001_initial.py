# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flowchart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=32, verbose_name='品名')),
                ('mold_num', models.CharField(max_length=32, verbose_name='模號')),
                ('cust_name', models.CharField(max_length=32, verbose_name='客戶名稱')),
            ],
            options={
                'verbose_name': '生產工藝流程卡',
                'verbose_name_plural': '生產工藝流程卡',
            },
        ),
        migrations.CreateModel(
            name='Flowchartprocess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=32, verbose_name='工序')),
                ('process_desc', models.CharField(max_length=128, verbose_name='過程描述')),
                ('flowchart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowchart.Flowchart')),
            ],
            options={
                'verbose_name': '流程',
                'verbose_name_plural': '流程',
            },
        ),
    ]