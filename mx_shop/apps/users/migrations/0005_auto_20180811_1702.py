# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-11 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180811_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='\u90ae\u7bb1'),
        ),
    ]