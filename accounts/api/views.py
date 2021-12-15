from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

from accounts.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_View(req):
    if req.method == 'POST':
        serialzer = RegistrationSerializer(data=req.data)
        data = {}
        if serialzer.is_valid():
            account = serialzer.save()
            data['response'] = "registration successful"
            data['email'] = account.email
            data['username'] = account.username
