# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0009_auto_20150620_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='authers',
            name='books',
            field=models.ManyToManyField(to='newapp2.Book'),
        ),
    ]
