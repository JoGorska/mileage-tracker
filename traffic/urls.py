'''urls for traffic messages app '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrafficMessagesList.as_view(), name='home'),
    path('add_traffic_msg', views.AddNewTrafficMsg.as_view(),
         name='add_traffic_msg'),
    path('thanks/<int:msg_id>', views.MsgThanks.as_view(), name='msg_thanks'),
]
