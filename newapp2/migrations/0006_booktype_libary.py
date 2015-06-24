# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0005_firstmodel_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Libary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numbers', models.IntegerField(max_length=10)),
                ('AveragePrice', models.IntegerField(max_length=3)),
                ('type', models.ForeignKey(to='newapp2.BookType')),
            ],
        ),
    ]
