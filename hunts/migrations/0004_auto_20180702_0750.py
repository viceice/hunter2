# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import hunts.models


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0003_merge_20180603_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(help_text='Include the URL of the file in solution content using $slug or ${slug}.', max_length=50)),
                ('file', models.FileField(upload_to=hunts.models.solution_file_path)),
            ],
        ),
        migrations.AddField(
            model_name='puzzle',
            name='soln_content',
            field=models.TextField(blank=True, default='', verbose_name='Solution content'),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='soln_runtime',
            field=models.CharField(choices=[('I', 'IFrame Runtime'), ('L', 'Lua Runtime'), ('R', 'Regex Runtime'), ('S', 'Static Runtime')], default='S', help_text='Runtime for generating the question solution', max_length=1, verbose_name='Solution runtime'),
        ),
        migrations.AddField(
            model_name='solutionfile',
            name='puzzle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunts.Puzzle'),
        ),
        migrations.AlterUniqueTogether(
            name='solutionfile',
            unique_together=set([('puzzle', 'slug')]),
        ),
    ]