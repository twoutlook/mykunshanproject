# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyreport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.DateField(verbose_name='員工姓名')),
                ('firstdate', models.DateField(verbose_name='報到日期')),
            ],
            options={
                'verbose_name_plural': '員工',
                'verbose_name': '員工',
            },
        ),
        migrations.CreateModel(
            name='Vocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocationnum', models.IntegerField(default=1, verbose_name='項次')),
                ('vocationfrom', models.DateField(verbose_name='起')),
                ('vocationto', models.DateField(verbose_name='止')),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyreport.Employee', verbose_name='員工姓名')),
            ],
            options={
                'verbose_name_plural': '休假',
                'verbose_name': '休假',
            },
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.CharField(max_length=500, verbose_name='說明'),
        ),
    ]