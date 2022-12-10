from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path('', views.ReportingOptionsView.as_view(), name='reporting_options'),
    path('period/', views.ChoosePeriodView.as_view(), name='choose_period'),
    path('period/', views.PeriodExcelView.as_view(), name='choose_period_excel'),
    path('period/<slug:start_date>/<slug:end_date>', views.PeriodReportView.as_view(), name='period_report'),  # noqa
    path('excell/<slug:start_date>/<slug:end_date>', views.excelExportJourneys.as_view(), name='excel_report'),  # noqa
    path("date/", views.DatePickerView.as_view(), name="choose_date"),
    path("date/<slug:slug>/", views.DayReport.as_view(), name="day_report"),
]
