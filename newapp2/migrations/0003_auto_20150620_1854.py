# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0002_firstmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstmodel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
        ),
    ]
