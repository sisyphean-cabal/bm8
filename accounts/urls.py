from django.urls import path
from .views import ProfileLookup, ProfileView
from . import views

urlpatterns = [
    path('profile/new', ProfileView.as_view(), name="Profile"),
    path('profile/list', ProfileLookup.as_view(), name="Lookup"),
]
