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

    # serializer_class = ProfileTokenSerialzer
    # if coreapi is not None and coreschema is not None:
    #     schema = ManualSchema(
    #         fields=[
    #             coreapi.Field(
    #                 name="email",
    #                 required=True,
    #                 location="form",
    #                 schema=coreschema.String(
    #                     title="Email",
    #                     description="Valid email for authentication",
    #                 ),
    #             ),
    #             coreapi.Field(
    #                 name="phone_number",
    #                 required=False,
    #                 location="form",
    #                 schema=coreschema.String(
    #                     title="Phonenumber",
    #                     description="Valid phone number for authentication",
    #                 ),
    #             ),
    #             coreapi.Field(
    #                 name="password",
    #                 required=True,
    #                 location="form",
    #                 schema=coreschema.String(
    #                     title="Password",
    #                     description="Valid password for authentication",
    #                 ),
    #             ),
    #         ],
    #         encoding="application/json",
    #     )
    # else:
    #     logging.error()


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
