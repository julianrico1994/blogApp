# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20170816_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='question',
        ),
        migrations.AddField(
            model_name='post',
            name='answer',
            field=models.TextField(default=b''),
        ),
    ]
