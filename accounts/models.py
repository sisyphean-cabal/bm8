from dataclasses import dataclass

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AbsUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        email = self.normalize_email(email)
        phone_number = phone_number
        user = self.model(email=email, phone_number=phone_number)
        return user

    def create_superuser(self, email_or_phone, password=None):
        pass


class AbsUserAccount(AbstractBaseUser):
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
