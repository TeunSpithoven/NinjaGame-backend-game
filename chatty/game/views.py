from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'chat/index.html')

# GAME

def game(request, game_name):
    username = request.GET.get('username', 'Anonymous')
    players = Player.objects.filter(gameName=game_name)
    shurikens = Shuriken.objects.filter(playerName=username)

    return (request, 
        {
            'game_name': game_name, 
            'username': username, 
            'players': players,
            'shurikens': shurikens
        })