# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-18 13:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihunt', '0004_teampuzzledata_userpuzzledata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampuzzledata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='userpuzzledata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]