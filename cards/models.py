# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from random import shuffle
from django.contrib.auth.models import User

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
    
    def getPlayers(self):
        return Player.objects.filter(game= self)

    def getPlayerCount(self):
        return self.getPlayers().latest('playerNum').playerNum

    def getCards(self):
        cards = Card.objects.filter()
        for i in cards:
            cardOwners(game=self, card=i).save()
    def dealCards(self):
        pass
        # whites = shuffle(list(Card.objects.filter(color="white")))
        # blacks = shuffle(list(Card.objects.filter(color="black")))
        # players = self.getPlayers()



class Player(models.Model):
    u_id = models.IntegerField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    playerNum = models.IntegerField()
    isDealer = models.IntegerField(default=0)

    def __str__(self):
        return "Name:   " + User.objects.get(id=self.u_id).username  + "    Game:   " + self.game.name

     

class cardOwners(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, default=0)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE, default=0)
    






