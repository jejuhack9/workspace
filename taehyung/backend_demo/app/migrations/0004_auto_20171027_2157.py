# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-27 12:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20171027_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_logo', models.FileField(upload_to='files/%Y%m%d/')),
                ('usr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='after_picture',
            field=models.FileField(default='No Picture', upload_to='files/%Y%m%d/'),
        ),
        migrations.AddField(
            model_name='reply',
            name='before_picture',
            field=models.FileField(default='No Picture', upload_to='files/%Y%m%d/'),
        ),
    ]