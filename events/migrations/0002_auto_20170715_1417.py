# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 13:17
from __future__ import unicode_literals

from django.db import migrations
import events.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='current',
            field=events.fields.SingleTrueBooleanField(),
        ),
    ]