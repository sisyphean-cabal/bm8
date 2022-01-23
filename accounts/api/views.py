from rest_framework import generics, parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import coreapi, coreschema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema

from accounts.api.serializers import LoginTokenSerializer, RegistrationSerializer, UserSerializer
from accounts.models import User


class ObtainLoginToken(ObtainAuthToken):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = LoginTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Email",
                        description="Valid Email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="phone_number",
                    required=False,
                    location="form",
                    schema=coreschema.String(
                        title="phone_number",
                        description="Valid phone number for authentication",
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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


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
