# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-28 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeju', '0004_auto_20171028_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csfile',
            name='file',
            field=models.FileField(upload_to='files/%Y%m%d/'),
        ),
    ]