# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-26 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_auto_20180417_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_level',
            field=models.IntegerField(blank=True, choices=[(1, 'manager 권한'), (2, 'family 권한'), (3, 'normal 권한')], default='3', null=True, verbose_name='권한레벨'),
        ),
    ]
