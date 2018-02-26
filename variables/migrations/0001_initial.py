# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=1000)),
                ('help_text', models.CharField(max_length=1000)),
            ],
        ),
    ]