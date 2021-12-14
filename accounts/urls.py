from django.urls import path
from .views import ProfileLookup, ProfileView
from . import views

urlpatterns = [
    path('profile', ProfileView.as_view(), name="Profile"),
    path('profile/lookup', ProfileLookup.as_view(), name="Lookup"),
]
