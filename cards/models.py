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


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)