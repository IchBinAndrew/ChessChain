from django.urls import path
from . import views
from .views import login_view, register_view, logout_view

app_name = "authentification"

urlpatterns = [
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view)
]