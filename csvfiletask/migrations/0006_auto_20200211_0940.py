# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-11 09:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('csvfiletask', '0005_auto_20200211_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 11, 9, 40, 19, 397937, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 11, 9, 40, 19, 397969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
