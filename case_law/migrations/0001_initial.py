# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 23:54
from __future__ import unicode_literals

import case_law.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateField()),
                ('pdf', models.FileField(upload_to='secure', validators=[case_law.models.Case.validate_file_extension], verbose_name='PDF')),
                ('synopsis', models.TextField()),
            ],
            options={
                'permissions': (('view_pdf', 'Can view PDF'),),
            },
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='headings',
            field=models.ManyToManyField(to='case_law.Heading'),
        ),
    ]