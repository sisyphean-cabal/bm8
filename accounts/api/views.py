from rest_framework import generics
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema

from accounts.api.serializers import (
    ProfileTokenSerialzer,
    RegistrationSerializer,
    UserSerializer,
)
from accounts.models import User


class UserAuthToken(auth_views.ObtainAuthToken):
    serializer_class = ProfileTokenSerialzer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
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
