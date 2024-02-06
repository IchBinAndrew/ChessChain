from django.urls import path
from . import views
from .views import login_view

app_name = "authentification"

urlpatterns = [
    path('login/', login_view)
]