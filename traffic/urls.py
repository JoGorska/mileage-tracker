from . import views
from django.urls import path

urlpatterns = [
    path('', views.TrafficMessagesList.as_view(), name='home'),
    path('add_traffic_msg', views.AddNewTrafficMsg.as_view(), name='add_traffic_msg'),
    path('thanks/<int:id>', views.MsgThanks.as_view(), name='msg_thanks'),
]
