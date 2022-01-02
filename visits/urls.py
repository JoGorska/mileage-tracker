from django.urls import path
from . import views


app_name = "visits"

urlpatterns = [

    path('', views.drive, name="drive"),
    path('map', views.map_view, name="map"),
    path('post_visit_data/<str:address_start>/<str:address_destination>/<str:distance>/', views.AddJourney.as_view(), name="post_visit"),

    path('date', views.DatePickerView.as_view(), name='date_picker'),
    path('date/<slug:slug>/', views.DateView.as_view(), name='date_view'),
    path('next_journey/<str:address_destination>/', views.drive_next_journey, name="next_journey"),
    path('next_journey/<str:address_destination>/map', views.map_view_next_journey, name="map_next_journey"),

    path('edit_journey/<int:journey_id>', views.drive_edit_journey, name="edit_journey"),
    path('edit_journey/<int:journey_id>/map', views.map_view_edit_journey, name="map_edit_journey"),
    path('edit_journey/<str:address_start>/<str:address_destination>/<str:distance>/', views.UpdateJourney.as_view(), name="post_update_visit"),
	]
