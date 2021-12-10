from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    name = models.CharField(max_length=500)


class Genre(models.Model):
    name = models.CharField(max_length=90)


class Band(models.Model):
    name = models.CharField(max_length=500)
    albums = models.ForeignKey(Album, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    albums = models.ManyToManyField(Album)
    band = models.ManyToManyField(Band)
