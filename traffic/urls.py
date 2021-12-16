from . import views
from django.urls import path

urlpatterns = [
    path('', views.TrafficMessagesList.as_view(), name='home')
]
