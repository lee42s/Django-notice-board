# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-11 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='관리자'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_member',
            field=models.BooleanField(default=False, verbose_name='회원'),
        ),
    ]