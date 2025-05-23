from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('signup/', views.user_signup, name="signup"),
]
