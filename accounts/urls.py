from django.urls import path
from .views import ProfileView
from . import views

urlpatterns = [
    path('profile', ProfileView.as_view(), name="Profile")
]
