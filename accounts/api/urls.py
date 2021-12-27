from django.urls import path

from accounts.api.views import RegisterLookUp, UserTokenLogin, registration_view

app_name = "account"

urlpatterns = [
    path("register", registration_view, name="register"),
    path("register/look", RegisterLookUp.as_view(), name="lookup"),
    path("login/token", UserTokenLogin.as_view()),
]
