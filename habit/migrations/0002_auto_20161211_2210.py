# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(default='Something', help_text='What is your goal?', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(help_text='When do you want to begin?'),
        ),
    ]
