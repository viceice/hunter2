# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import hunts.models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20170425_1400'),
        ('hunts', '0040_populate_guess_by_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='by_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
    ]
