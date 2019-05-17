# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 11:53
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_watchedquery'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='maintainers',
            field=jsonfield.fields.JSONField(blank=True, default=[], dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}),
        ),
    ]