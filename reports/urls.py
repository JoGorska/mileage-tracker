from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path('', views.ReportingOptionsView.as_view(), name='reporting_options'),
    path('period/', views.ChoosePeriodView.as_view(), name='choose_period'),
    path("date/", views.DatePickerView.as_view(), name="choose_date"),
    path("date/<slug:slug>/", views.DayReport.as_view(), name="day_report"),
]
