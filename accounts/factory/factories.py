import factory
from faker import Faker

from accounts.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    # user table
    class Meta:
        model = User.objects.all

    phone_numer = fake.phone_number()
    password = fake.password()
    email = fake.email()
