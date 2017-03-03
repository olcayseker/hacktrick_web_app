# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 12:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hacktrick', '0003_auto_20170302_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='instructor',
            field=models.ManyToManyField(related_name='trainings', related_query_name='training', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(help_text='370x190', upload_to='sponsor/'),
        ),
    ]