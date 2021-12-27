from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from accounts.models import User


class ProfileTokenSerialzer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_(
            "Password",
        ),
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)

            if not user:
                msg = _("Login credentials not found. Did you enter the correct email address of password?")
                raise serializers.ValidationError(msg, code="authorization")

        else:
            msg = _("Must include email and password fields")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "groups",
            "user_permissions",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        )


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password_confirmation = serializers.CharField(max_length=280)

    class Meta:
        model = User
        fields = ["email", "phone_number", "password", "password_confirmation"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        keys = {}
        if "email" in self.validated_data:
            keys["email"] = self.validated_data["email"]
        if "phone_number" in self.validated_data:
            keys["phone_number"] = self.validated_data["phone_number"]
        account = User(**keys)
        password = self.validated_data["password"]

        account.set_password(password)
        account.save()
        return account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "phone_number", "password")
