from django.urls import path
from . import views

urlpatterns = [
    path("", views.social_login, name="social_login"),
]
