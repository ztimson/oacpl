# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0003_subscriber_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]