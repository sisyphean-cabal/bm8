import factory
from faker import Faker

from accounts.models import User

fake = Faker()


class UserFct(factory.django.DjangoModelFactory):

    # user table
    class Meta:
        model = User

    phone_numer = fake.phone_number()
    email = fake.email()
