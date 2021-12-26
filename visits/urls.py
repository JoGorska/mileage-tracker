from django.urls import path
from . import views


app_name = "visits"

urlpatterns = [

    path('', views.drive, name="drive"),
    path('map', views.map_view, name="map"),
	]

# from . import views
# from django.urls import path
# from .views import DateView

# urlpatterns = [

#     path('', views.DatePickerView.as_view(), name='date_picker'),
#     path('<str:date_string>/', views.DateView.as_view(), name='date_view'),
# ]