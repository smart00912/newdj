# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='isactive',
            field=models.BooleanField(default=0),
        ),
    ]
