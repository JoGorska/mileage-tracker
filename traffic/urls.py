from . import views
from django.urls import path

urlpatterns = [
    path('', views.TrafficMessagesList.as_view(), name='home'),
    path('<int:id>/', views.TrafficMsgDetail.as_view(), name='traffic_msg_detail'),
    path('add_traffic_msg', views.AddNewTrafficMsg.as_view(), name='add_traffic_msg'),
    path('thanks/<int:id>', views.MsgThanks.as_view(), name='msg_thanks'),
    # path('cleared/<int:id>', views.MsgCleared.as_view(), name='msg_cleared'),
]
