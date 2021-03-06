# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortItURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, validators=[shortner.validators.validate_url, shortner.validators.validate_dot_com])),
                ('shortcode', models.CharField(blank=True, max_length=6, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
