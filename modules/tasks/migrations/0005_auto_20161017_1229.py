# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20161017_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='plan_date',
            field=models.DateTimeField(default='timezone.now()', verbose_name='Planlanan Tarih'),
        ),
    ]
