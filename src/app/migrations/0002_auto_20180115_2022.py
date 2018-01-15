# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_to_live',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ttl_option',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(None, b'----'), (b'minutes=10', b'10 minutes'), (b'hours=1', b'1 hour'), (b'days=1', b'1 day'), (b'days=7', b'1 week'), (b'days=30', b'1 month')]),
        ),
    ]
