# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstmodel',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 20, 18, 52, 46, 104000), blank=True),
        ),
    ]
