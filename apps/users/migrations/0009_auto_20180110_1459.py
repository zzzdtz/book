# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_commentmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodels',
            name='comment_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='评论时间'),
        ),
    ]
