# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20180114_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='topic',
            new_name='name',
        ),
    ]