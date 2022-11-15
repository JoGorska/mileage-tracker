from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import RegisterUserView
from . import views

app_name = "users"

urlpatterns = [

    path("register", RegisterUserView.as_view(), name="register"),
    path("user_profile", views.UserProfileView.as_view(), name="user_profile"),
    path(
        "edit_profile/<int:user_id>",
        views.EditProfile.as_view(), name="edit_profile"
    ),
    path(
        "accounts/login",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
]
