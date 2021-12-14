import os
from django.views import ProfileLookup, ProfileLookupView, ProfileNewView, ProfileView
from django.urls import path
from django.db.models import Profiles


class UserData:
    def user_name(name):
        name = name;
        print(name)


x = UserData()
x.user_name;
