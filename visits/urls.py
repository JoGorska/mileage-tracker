from django.urls import path
from . import views


app_name = "visits"

urlpatterns = [
    
    path('drive', views.DatePickerDrive.as_view(), name="date_picker_drive"),
    path('drive/<slug:slug>/ready/', views.drive_date_ready, name='drive_date_ready'),
    path('drive/<slug:slug>/calc-distance/', views.calculate_distance, name="calc-distance"),

    # post visit data is for the form to post data in database and return user to drive/slug/next_journey.
    # need to fill in the start address => postcode and date from datepicker model from slug
    path('post_visit_data/<str:address_start>/<str:address_destination>/<str:distance>/', views.AddJourney.as_view(), name="post_visit"),

    path('date', views.DatePickerView.as_view(), name='date_picker'),
    path('date/<slug:slug>/', views.DateView.as_view(), name='date_view'),

    
    # need to fill in the start address => postcode and date from datepicker model from slug
    # url needs to change drive/<slug:slug>/next_journey/<str:addres_destination>/
    path('next_journey/<str:address_destination>/', views.drive_next_journey, name="next_journey"),

    path('edit_journey/<int:journey_id>', views.drive_edit_journey, name="edit_journey"),
    path('edit_journey/<int:journey_id>/<str:address_start>/<str:address_destination>/<str:distance>', views.UpdateJourney.as_view(), name="post_update_visit"),
	]
