from django.urls import path
from django.urls.resolvers import URLPattern
from accounts.api.views import(
    registration_view,
)

app_name = "account"

urlpatterns = [
    path('register', registration_view, name="register"),
]