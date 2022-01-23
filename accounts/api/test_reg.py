import json

from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory

from accounts.api.views import registration_view


class RegisterTest(TestCase):
    client = APIClient()
    factory = APIRequestFactory()

    def test_register_fail(self):
        data = {"email": "", "phone": "", "password": "wordpass", "password_confirmation": "wordpizzle"}
        req = self.factory.post("/api/account/register", json.dumps(data), content_type="application/json")
        view = registration_view
        res = view(req)

        # why is this test returning 200?
        self.assertEqual(res.status_code, 400)

    def test_register_success(self):
        data = {"email": "test@site.com", "phone": "", "password": "lol134", "password_confirmation": "lol134"}
        req = self.factory.post("/api/account/register", json.dumps(data), content_type="application/json")
        view = registration_view
        res = view(req)

        # Test should be 200.

        self.assertEqual(res.status_code, 200)

    # def test_register_attempt(self):
    #     data = {"email": "test@site.com", "phone": "", "password": "lol134", "password_confirmation": "lol134"}
    #     req = self.factory.post("/api/account/register", json.dumps(data), content_type="application/json")
    #     view = registration_view
