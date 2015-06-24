# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0011_auto_20150620_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authers',
            name='age',
            field=models.SmallIntegerField(help_text=b'Must between 20 to 100', null=True),
        ),
    ]
