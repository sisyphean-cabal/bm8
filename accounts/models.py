import uuid
from dataclasses import dataclass

from django import forms
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

"""
TODO
Remove password from AbsUserAccount.

UserIdentity
------------
AbsUserManager needs to create the UUID for the user and store it in the
identity table.

"""


class AbsUserManager(BaseUserManager):
    def prep_create_user(
        self,
        email_or_phone,
        is_staff,
        is_superuser,
        password=None,
        **extra_fields,
    ):

        if not email_or_phone:
            raise ValueError("You must give either a email or phone number")

        if "@" in email_or_phone:
            email_or_phone = self.normalize_email(email_or_phone)
            email, phone = (email_or_phone, "")

        else:
            # validation is handled by the frontend atm
            phone = email_or_phone

        user = self.model(
            email=email,
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save()

        return user

    def create_user(self, email_or_phone, password=None, **extra_fields):
        return self.prep_create_user(email_or_phone, False, False, password, **extra_fields)

    def create_superuser(self, email_or_phone, password=None, **extra_fields):
        return self.prep_create_user(email_or_phone, True, True, password, **extra_fields)


class UserIdentity(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id_type = models.CharField(default="")

    def __str__(self):
        return self.user_id


class AbsUserAccount(AbstractBaseUser):
    identity = models.ForeignKey(UserIdentity, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)

    @dataclass
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_email_or_phone_number",
                check=(models.Q(phone_number__isnull=False) | models.Q(email__isnull=False)),
            )
        ]

        def __str__(self):
            if self.email:
                return self.email
            else:
                return self.phone_number


class UserCredentials(models.Model):
    password = forms.CharField(widget=forms.PasswordInput)
    account = models.ForeignKey(AbsUserAccount, on_delete=models.CASCADE)
