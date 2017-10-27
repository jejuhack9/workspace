# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_reply_after_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporation',
            name='corp_descriptioin',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='corporation',
            name='corp_name',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AlterField(
            model_name='reply',
            name='after_picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='before_picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]