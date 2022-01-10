from django.urls import path
from . import views


app_name = "visits"

urlpatterns = [
    
    path('drive', views.DatePickerDrive.as_view(), name="date_picker_drive"),
    path('drive/<slug:slug>/ready/', views.Drive.as_view(), name='drive_date_ready'),

    path('drive/<slug:slug>/add_journey', views.AddJourney.as_view(), name="add_journey"),

    path('date', views.DatePickerView.as_view(), name='date_picker'),
    path('date/<slug:slug>/', views.DayReport.as_view(), name='day_report'),
       
    path('edit_journey/<slug:slug>/<int:journey_id>', views.EditJourney.as_view(), name="edit_journey"),
    path('edit_journey/<slug:slug>/<int:journey_id>', views.EditJourney.as_view(), name="post_changes_journey"),
	]
