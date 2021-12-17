from django.http import request
from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from accounts.api.views import registration_view
import json