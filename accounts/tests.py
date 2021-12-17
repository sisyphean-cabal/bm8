
from django.http import request
from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from accounts.api.views import registration_View
import json
class RegisterTest(TestCase):
    client = APIClient()
    factory = APIRequestFactory()

    def register_test(self):
        data = {'password': 'Lol123', 'password_confirmation': 'lol341'}
        req = self.factory.post('/api/accounts/register', json.dumps(data), content_type='applicat/json')
        view = registration_View.as_view()
        res = view(req)
        self.assertEqual(res.status, 400)


