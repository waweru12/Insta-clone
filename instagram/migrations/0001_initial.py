# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-21 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='instagram/')),
                ('image_name', models.CharField(max_length=60)),
                ('caption', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=500)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('profile_pic', models.ImageField(upload_to='instagram/')),
                ('bio', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
    ]
