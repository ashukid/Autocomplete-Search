# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-27 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]