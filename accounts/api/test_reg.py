from django.http import request
from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from accounts.api.views import registration_View
from djangorestframework_camel_case.parser import CamelCaseJSONParser
import json

class RegisterTest(TestCase):
    client = APIClient()
    factory = APIRequestFactory()

    def test_register(self):
        data = {'password': 'Lol124', 'password_confirmation': 'lol344'}
        req = self.factory.post('/api/accounts/register', json.dumps(data), content_type='application/json')
        view = registration_View
        print(req.body)
        res = view(req)
        self.assertEqual(res.status_code, 400)
