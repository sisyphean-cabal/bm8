from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    email = models.CharField(max_length=200, null=True, blank=True, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_email_or_phone_number",
                check=(models.Q(phone_number__isnull=False) | models.Q(email__isnull=False)),
            )
        ]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
