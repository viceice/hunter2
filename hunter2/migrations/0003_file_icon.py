# Generated by Django 3.1.5 on 2021-01-23 12:44

from django.db import migrations, models
import django.db.models.deletion
import hunter2.models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter2', '0002_auto_20200718_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('file', models.FileField(help_text='The extension of the uploaded file will determine the Content-Type of the file when served', upload_to=hunter2.models.file_path)),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(help_text='The size of the icon (width and height). 0 should be used for scalable (eg. SVG) icons.', unique=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunter2.file')),
            ],
        ),
    ]