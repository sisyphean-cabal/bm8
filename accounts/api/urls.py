from django.urls import path
from django.urls.resolvers import URLPattern
from accounts.api.views import(
    registration_View,
)

app_name = "account"

urlpatterns = [
    path('register', registration_View, name="register"),
]