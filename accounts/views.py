from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from accounts import serializers
# Create your views here.


class ProfileNewView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileLookupView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




