# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20170303_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='instructor/'),
        ),
    ]