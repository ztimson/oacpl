# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 01:28
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
