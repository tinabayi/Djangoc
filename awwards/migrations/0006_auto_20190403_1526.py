# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0005_auto_20190403_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='project_description',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='project_url',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
