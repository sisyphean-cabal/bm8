from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

class Profile(models.Model):
    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=1500)
    soundcloud = models.CharField(max_length=280)
    phone_number = PhoneNumberField(blank=True)

class User(AbstractBaseUser):
    email = models.CharField(max_length=200, null=True, blank=True, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)


    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_userna_isnull=Falseme_phonenumber",
                check=(~models.Q(phone_number__isnull=False, email_isnull=False))
            )
        ]


