from copy import error
from django.http.response import HttpResponse
from rest_framework import generics
from rest_framework import serializers
from rest_framework import response
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status
from django.shortcuts import render
from accounts.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_View(req):
    if req.method == 'POST':
        serializer = RegistrationSerializer(data=req.data)
        data = {}
        if req.data.password != req.data.password_confirmation:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "registration successful"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)
        
