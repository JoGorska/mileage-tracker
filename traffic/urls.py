from . import views
from django.urls import path

urlpatterns = [
    path('', views.TrafficMessagesList.as_view(), name='home'),
    path('<int:id>/', views.TrafficMsgDetail.as_view(), name='traffic_msg_detail'),
]
