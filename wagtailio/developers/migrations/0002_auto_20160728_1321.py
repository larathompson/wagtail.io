# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developerspageoptions',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelTable(
            name='developerspage',
            table=None,
        ),
        migrations.AlterModelTable(
            name='developerspageoptions',
            table=None,
        ),
    ]
