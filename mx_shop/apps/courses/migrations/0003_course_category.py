# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-09 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='\u5f8c\u7aef\u958b\u767c', max_length=20, verbose_name='\u8bfe\u7a0b\u985e\u5225'),
        ),
    ]
