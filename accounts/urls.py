from django.urls import path
from .views import ProfileLookupView, ProfileNewView
from . import views

urlpatterns = [
    path('profile/new', ProfileNewView.as_view(), name="Profile"),
    path('profile/list', ProfileLookupView.as_view(), name="Lookup"),
]
