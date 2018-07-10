# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-22 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestmodel',
            name='suggestType',
            field=models.IntegerField(choices=[(1, '建议'), (2, '纠正')], default=1, help_text='建议类型', verbose_name='建议类型'),
        ),
    ]
