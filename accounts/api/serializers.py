from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from accounts.models import User


class LoginTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True,
    )
    phone_number = PhoneNumberField(
        label=_("Phone number"),
        trim_whitespace=False,
        write_only=True,
    )
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)
        elif phone_number and password:
            user = authenticate(request=self.context.get("request"), phone_number=phone_number, password=password)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
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
