from django.urls import path
from . import main_views

urlpatterns = [
    path("login/", main_views.login_view, name="login"),
]