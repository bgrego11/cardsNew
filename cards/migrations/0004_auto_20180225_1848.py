# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20180225_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardowners',
            name='isDealer',
        ),
        migrations.RemoveField(
            model_name='cardowners',
            name='playerNum',
        ),
        migrations.RemoveField(
            model_name='cardowners',
            name='u_id',
        ),
        migrations.AddField(
            model_name='cardowners',
            name='card',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cards.Card'),
        ),
        migrations.AddField(
            model_name='cardowners',
            name='player',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cards.Player'),
        ),
    ]
