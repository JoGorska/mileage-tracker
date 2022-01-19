from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
        path('user_profile', views.UserProfile.as_view(), name="user_profile"),
        path('edit_profile/<int:user_id>', views.EditProfile.as_view(), name="edit_profile"),
]