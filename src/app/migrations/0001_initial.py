# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(unique=True)),
                ('code', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time_to_live', models.DateTimeField(blank=True)),
                ('ttl_option', models.CharField(blank=True, max_length=10, null=True, choices=[(None, b'----'), (b'minutes=10', b'10 minutes'), (b'hours=1', b'1 hour'), (b'days=1', b'1 day'), (b'days=7', b'1 week'), (b'days=30', b'1 month')])),
            ],
        ),
        migrations.CreateModel(
            name='Syntax',
            fields=[
                ('syntax_id', models.AutoField(serialize=False, primary_key=True)),
                ('syntax_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='syntax',
            field=models.ForeignKey(to='app.Syntax'),
        ),
    ]
