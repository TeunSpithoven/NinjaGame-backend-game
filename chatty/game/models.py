from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField
    startDate = models.DateTimeField
    endDate = models.DateTimeField

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    gameName = models.CharField(max_length=255, default="")
    health = models.IntegerField
    points = models.IntegerField
    posX = models.IntegerField
    posY = models.IntegerField

class Shuriken(models.Model):
    id = models.AutoField(primary_key=True)
    playerName = models.CharField
    posX = models.IntegerField
    posY = models.IntegerField    

