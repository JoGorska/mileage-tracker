from . import views
from django.urls import path
from .views import DateView

urlpatterns = [

    path('', views.DatePickerView.as_view(), name='date_picker'),
    path('<str:date_to_string>/', views.DateView.as_view(), name='date_view'),
]
