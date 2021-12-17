from django.http import request
from django.test import TestCase, Client
from rest_framework.decorators import api_view
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from accounts.api.views import registration_View
import json

class RegisterTest(TestCase):
    client = APIClient()
    factory = APIRequestFactory()

    def test_register(self):
        data = {'password': 'Lol124', 'passwordConfirmation': 'lol344'}
        req = self.factory.post('/api/accounts/register', json.dumps(data), content_type='application/json')
        view = registration_View
        print(req.body)
        res = view(req)
        self.assertEqual(res.status_code, 400)
