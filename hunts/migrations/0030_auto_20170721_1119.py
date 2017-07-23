# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0029_auto_20170717_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='headstart_from',
            field=models.ManyToManyField(blank=True, help_text='Episodes which should grant a headstart for this episode', to='hunts.Episode'),
        ),
    ]