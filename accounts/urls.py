from django.urls import path
from .views import ProfileView
from . import views

urlpatterns = [
    path('api', ProfileView.as_view(), name="Profile")
]
