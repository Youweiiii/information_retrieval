# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0002_auto_20170408_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.RemoveField(
            model_name='job',
            name='date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='jobtitle',
        ),
        migrations.RemoveField(
            model_name='job',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='job',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='job',
            name='source',
        ),
        migrations.RemoveField(
            model_name='job',
            name='url',
        ),
    ]