from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
        path('user_profile', views.UserProfile.as_view(), name="user_profile"),
]