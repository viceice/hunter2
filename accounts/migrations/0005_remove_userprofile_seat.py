# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180513_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='seat',
        ),
    ]
