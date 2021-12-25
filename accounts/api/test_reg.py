from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from accounts.api.views import registration_view
import json


class RegisterTest(TestCase):
    client = APIClient()
    factory = APIRequestFactory()

    def test_register(self):
        data = {"password": "Lol124", "password_confirmation": "lol344"}
        req = self.factory.post(
            "/api/account/register", json.dumps(data), content_type="application/json"
        )
        view = registration_view
        print(req.body)
        res = view(req)
        self.assertEqual(res.status_code, 400)
