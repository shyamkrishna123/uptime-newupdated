# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addServer', '0002_remove_addserver_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='addserver',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]