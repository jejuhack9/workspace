# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-28 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171028_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
