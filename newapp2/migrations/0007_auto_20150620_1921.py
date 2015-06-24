# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0006_booktype_libary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libary',
            name='AveragePrice',
        ),
        migrations.RemoveField(
            model_name='libary',
            name='numbers',
        ),
    ]
