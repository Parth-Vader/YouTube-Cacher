# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_localhost', models.CharField(max_length=200)),
                ('on_network', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_time', models.DateTimeField(verbose_name='time of request')),
                ('requester', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_site', models.CharField(max_length=200)),
                ('video_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together=set([('video_site', 'video_id')]),
        ),
        migrations.AddField(
            model_name='request',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeper.Video'),
        ),
        migrations.AddField(
            model_name='location',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeper.Video'),
        ),
    ]
