# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-11 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20180411_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_none_member',
            field=models.BooleanField(default=True, verbose_name='비회원'),
        ),
    ]