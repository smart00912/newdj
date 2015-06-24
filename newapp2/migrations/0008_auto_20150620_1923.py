# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0007_auto_20150620_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='libary',
            name='AveragePrice',
            field=models.IntegerField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='libary',
            name='numbers',
            field=models.IntegerField(max_length=3, null=True),
        ),
    ]
