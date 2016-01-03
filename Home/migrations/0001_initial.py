# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('text', models.TextField(default='')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='w', max_length=1)),
                ('description', models.TextField(default='', max_length=300)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Home.Post'),
        ),
    ]
