"""bm8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# YASG related
schema_v = get_schema_view(
    openapi.Info(
        title="Riff API",
        default_version="0.0.1",
        description="Endpoints for Armageddon",
        terms_of_service="uwaht",
        contact=openapi.Contact(email="Bryan@yiffriffrippers.org"),
        license=openapi.License(name="BSD or some shit"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # REST
    path("api/account/", include("accounts.api.urls", "account_api")),
    # YASG
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_v.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_v.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_v.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
