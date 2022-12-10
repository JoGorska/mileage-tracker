from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path('', views.ReportingOptionsView.as_view(), name='reporting_options'),

    # date pickers
    path('period/', views.ChoosePeriodView.as_view(), name='choose_period'),
    path('excell/', views.PeriodExcelView.as_view(), name='choose_period_excel'),
    path("date/", views.DatePickerView.as_view(), name="choose_date"),

    # reports
    path('period/<slug:start_date>/<slug:end_date>', views.PeriodReportView.as_view(), name='period_report'),  # noqa
    path('excell/<slug:start_date>/<slug:end_date>', views.ExcelExportJourneys.as_view(), name='excel_report'),  # noqa
    path("date/<slug:slug>/", views.DayReport.as_view(), name="day_report"),
]
