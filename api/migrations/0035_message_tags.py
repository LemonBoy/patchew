# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-27 10:09
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20180822_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='tags',
            field=jsonfield.fields.JSONField(default=[], dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}),
        ),
    ]
