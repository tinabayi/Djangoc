# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='project_description',
            field=models.TextField(null=True),
        ),
    ]
