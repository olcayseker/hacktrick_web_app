# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20170303_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='facebook',
            field=models.CharField(blank=True, help_text='facebook kullanıcı adı', max_length=50),
        ),
        migrations.AddField(
            model_name='instructor',
            name='linkedin',
            field=models.CharField(blank=True, help_text='linkedin kullanıcı adı', max_length=50),
        ),
        migrations.AddField(
            model_name='instructor',
            name='twitter',
            field=models.CharField(blank=True, help_text='twitter kullanıcı adı', max_length=50),
        ),
    ]
