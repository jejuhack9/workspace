# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 16:24
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171028_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='after_picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
