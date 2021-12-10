from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    name = models.CharField(max_length=500)


class Bands(models.Model):
    name = models.CharField(max_length=500)
    albums = models.ManyToManyField(Album)


class Genres(models.Model):
    name = models.CharField(max_length=90)
    bands = models.ManyToManyField(Bands)
    albums = models.ManyToManyField(Album)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres)
