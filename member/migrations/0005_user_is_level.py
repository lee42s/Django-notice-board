# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-16 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_remove_user_is_none_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_level',
            field=models.CharField(blank=True, choices=[(1, '목록보기'), (2, '글작성'), (3, '상세보기'), (4, '댓글작성')], max_length=8, null=True),
        ),
    ]