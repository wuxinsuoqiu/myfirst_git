# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-09 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_teacher_image'),
        ('courses', '0007_auto_20180809_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u8bb2\u5e08'),
        ),
    ]
