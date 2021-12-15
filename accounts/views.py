from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile
from .api.serializers import ProfileSerializer
# Create your views here.


class ProfileNewView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileLookupView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




