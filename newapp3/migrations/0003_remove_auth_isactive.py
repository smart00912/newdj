# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp3', '0002_auth_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auth',
            name='isactive',
        ),
    ]
