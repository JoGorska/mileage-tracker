from . import views
from django.urls import path
from .views import DateView

urlpatterns = [

    path('<slug:date_slug>/', views.DateView.as_view(), name='date_picker'),
]