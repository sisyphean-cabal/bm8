import factory
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractBaseUser

    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        self.set_password(self.password)
        self.save()
