# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django import forms
from .forms import UserRegistrationForm, NewGameForm, JoinGameForm
from django.contrib.auth.models import User
from .models import Game, Player
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse


def index(request):
    gameIds = list(Player.objects.filter(u_id=request.user.id).values_list('game', flat=True))
    
    games = list(Game.objects.filter(id__in=gameIds))
    # games = playerObs.
    # for i in games:
    #     print i.name
    return render(request, 'cards/home.html', context={'user': request.user,'games' : games})



#pass game objects into cards page

def newGame(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST)
        if form.is_valid():
            gameObj = form.cleaned_data
            name = gameObj['name']
            password =  gameObj['password']
            host =  gameObj['host']
            g = Game(name = name, password = password, host=host)
            g.save()
            Player(u_id=g.host, game=g, playerNum = 1).save()
            return render(request, 'cards/gamePlay.html', {'game' : g})

def joinGame(request):
    if request.method == 'POST':
        form = JoinGameForm(request.POST)
        if form.is_valid():
            gameObj = form.cleaned_data
            name = gameObj['name']
            password =  gameObj['password']
            player =  gameObj['player']
            try:
                game = Game.objects.get(name=name, password=password)
                if game is not None:
                    if game.getPlayerCount() < 6:
                        Player(u_id=player, game=game, playerNum = game.getPlayerCount()+1 ).save()
                        return render(request, 'cards/gamePlay.html', {'game' : game})
                    else:
                        return redirect(index)
            except:
                return redirect(index)


            # g = Game(name = name, password = password, host=host)
            # g.save()
            # Player(u_id=g.host, game=g, playerNum = 1).save()
            # return render(request, 'cards/gamePlay.html', {'game' : g})



            #return game page with game object attached

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/cards')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'cards/register.html', {'form' : form})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'home.html', {'form': form})
