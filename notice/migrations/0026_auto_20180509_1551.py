# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-09 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0025_auto_20180509_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imges',
            name='imges',
            field=models.ImageField(blank=True, default='static/img/noimg.jpg', upload_to='imges/%Y/%m/%d/'),
        ),
    ]
