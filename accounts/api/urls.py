from django.urls import path

from accounts.api.views import RegisterLookUp, UserAuthToken, registration_view

app_name = "account"

urlpatterns = [
    path("register", registration_view, name="register"),
    path("register/look", RegisterLookUp.as_view(), name="lookup"),
    path("register/api-token-auth/", UserAuthToken.as_view()),
]
