from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.api.serializers import RegistrationSerializer, UserSerializer
from accounts.models import User


@api_view(["POST"])
def registration_view(req):
    if req.method == "POST":
        serializer = RegistrationSerializer(data=req.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "registration successful"
            data["email"] = account.email
            data["phone_number"] = str(account.phone_number)
            # token = Token.objects.get(user=account).key
            # data["token"] = token
        else:
            data = serializer.errors
        return Response(data)


class RegisterLookUp(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
