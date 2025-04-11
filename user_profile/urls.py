from django.urls import path
from . import views

app_name = "user_profile"

urlpatterns = [
    path('<str:username>/', views.user_profile, name="user_profile"),
]
