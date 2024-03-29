# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charter_members', '0004_attorney_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chapter',
            new_name='Region',
        ),
        migrations.RenameField(
            model_name='attorney',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='attorney',
            old_name='chapter',
            new_name='region',
        ),
        migrations.AddField(
            model_name='attorney',
            name='address',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attorney',
            name='call_to_bar',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attorney',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attorney',
            name='lso',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='joined',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
