# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 21:21
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0030_auto_20170312_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'Kayıt'), (1, 'Eğitim seçimi'), (2, 'Eğitim onayı'), (3, 'Eğitimin güncellenmesi'), (4, 'Eğitime döküman eklenmesi'), (5, 'Bir kullanıcının eğitmen olarak işaretlenmesi'), (6, 'Eğitime kesin kayıt olunması'), (7, 'Ticket açılması'), (8, 'Ticketa cevap verilmesi')], verbose_name='Mail seçimi')),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik')),
            ],
        ),
    ]