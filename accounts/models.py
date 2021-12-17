from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from phonenumber_field.modelfields import PhoneNumberField

class Album(models.Model):
    name = models.CharField(max_length=500)


class Genre(models.Model):
    name = models.CharField(max_length=90)


class Band(models.Model):
    name = models.CharField(max_length=500)
    albums = models.ForeignKey(Album, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)


class Profile(models.Model):
    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=1500)
    soundcloud = models.CharField(max_length=280)
    phone_number = PhoneNumberField(blank=True)

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             name="%(app_label)s_%(class)s_username_phonenumber",
    #             check=(models.phone)
    #         )
    #     ]

