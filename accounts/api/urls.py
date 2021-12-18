from django.urls import path
from django.urls.resolvers import URLPattern
from accounts.api.views import(
    RegisterLookUp,
    registration_view,
)

app_name = "account"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('register/look', RegisterLookUp.as_view(), name="lookup")
]