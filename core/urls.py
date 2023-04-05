from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeTempaltes.as_view(), name="home"),
]
