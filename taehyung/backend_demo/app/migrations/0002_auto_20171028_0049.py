# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 15:49
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='after_picture',
        ),
        migrations.AlterField(
            model_name='reply',
            name='before_picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
