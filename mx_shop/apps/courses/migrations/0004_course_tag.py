# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-09 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='\u8ab2\u7a0b\u6a19\u7c64'),
        ),
    ]