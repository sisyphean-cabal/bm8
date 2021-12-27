from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.api.serializers import RegistrationSerializer, UserSerializer
from accounts.models import User


class UserTokenLogin(ObtainAuthToken):
    def post(self, req, *args, **kwargs):
        serializer = self.serializer_class(data=req.data, context={"request:", req})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["User"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "email": user.email,
                "phone": user.phone_number,
            }
        )


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
        else:
            data = serializer.errors
        return Response(data)


class RegisterLookUp(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
