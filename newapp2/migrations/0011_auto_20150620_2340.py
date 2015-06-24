# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0010_auto_20150620_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstmodel',
            name='gender',
            field=models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Famile')]),
        ),
    ]
