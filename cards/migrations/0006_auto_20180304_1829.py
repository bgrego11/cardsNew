# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20180302_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='host',
            field=models.IntegerField(),
        ),
    ]