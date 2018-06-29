# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='by_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.Team'),
        ),
    ]
