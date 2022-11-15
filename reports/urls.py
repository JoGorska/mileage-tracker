from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path('', views.ReportView.as_view(), name='reports_view'),
]
