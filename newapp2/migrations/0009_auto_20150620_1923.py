# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0008_auto_20150620_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libary',
            name='AveragePrice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='libary',
            name='numbers',
            field=models.IntegerField(null=True),
        ),
    ]
