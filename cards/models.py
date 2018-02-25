# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Card(models.Model):
    text = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    options = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text


class Game(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    host = models.IntegerField()
    isFull = models.IntegerField(default=0)
    isStarted = models.IntegerField(default=0)
    isPaused = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Players(models.Model):
    u_id = models.IntegerField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    playerNum = models.IntegerField()
    isDealer = models.IntegerField(default=0)






