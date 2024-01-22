"""Define URL patterns for core."""
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", LogoutView.as_view(), name="logout"),
]
