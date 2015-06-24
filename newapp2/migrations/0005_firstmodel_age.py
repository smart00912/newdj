# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0004_auto_20150620_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstmodel',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
