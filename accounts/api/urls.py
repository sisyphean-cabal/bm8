from django.urls import path
from rest_framework.authtoken import views

from accounts.api.views import RegisterLookUp, registration_view

app_name = "account"

urlpatterns = [
    path("register", registration_view, name="register"),
    path("register/look", RegisterLookUp.as_view(), name="lookup"),
    path("login/token", views.obtain_auth_token),
]
