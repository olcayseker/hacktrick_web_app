# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170313_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='institution',
            field=models.CharField(max_length=100, verbose_name='Kurum'),
        ),
    ]
