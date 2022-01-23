import pytest
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory


class RegisterTest(TestCase):

    client = APIClient()
    factory = APIRequestFactory()

    @pytest.mark.django_db
    def test_new_user(account_factory):
        assert True

    # def test_register_post_success(self):

    #     data = {"email": "test@site.com", "phone": "", "password": "lol134", "password_confirmation": "lol134"}
    #     req = self.factory.post("/api/account/register", json.dumps(data), content_type="application/json")
    #     view = registration_view
    #     res = view(req)

    #     # Test should be 200.

    #     self.assertEqual(res.status_code, 200)
