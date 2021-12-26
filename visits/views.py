from datetime import datetime
from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


from .models import Journey, DatePicker
from .forms import JourneyForm, DatePickerForm
from .mixins import Directions


def drive(request):
    """
    Basic view for adding start and destination
    created by following 
    https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
    """

    context = {"google_api_key": settings.GOOGLE_API_KEY}
    return render(request, 'visits/drive.html', context)


def map_view(request):
    """
    Basic view for displaying a map
    created by following 
    https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
    """

    lat_a = request.GET.get("lat_a")
    long_a = request.GET.get("long_a")
    lat_b = request.GET.get("lat_b")
    long_b = request.GET.get("long_b")
    directions = Directions(
        lat_a=lat_a,
        long_a=long_a,
        lat_b=lat_b,
        long_b=long_b
        )

    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
        "lat_a": lat_a,
        "long_a": long_a,
        "lat_b": lat_b,
        "long_b": long_b,
        "origin": f'{lat_a}, {long_a}',
        "destination": f'{lat_b}, {long_b}',
        "directions": directions,
    }
    return render(request, 'visits/map.html', context)


# class DatePickerView(View):
#     template_name = 'visits/date_picker.html'
#     form_class = DatePickerForm

#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             'visits/date_picker.html',
#             {
#                 'date_picker_form': DatePickerForm()
#             },
#         )

#     def post(self, request, *args, **kwargs):

#         date_picker_form = DatePickerForm(data=request.POST)


#         if date_picker_form.is_valid():

#             date_picked_record = date_picker_form.save(commit=False)
#             date_picked_record.save('date_picked')
#             date_picked = request.POST.get('date_picked')
#             print(date_picked_record)


#             date_string = str(date_picked)

#             print(date_string)

#             # return reverse('date_view', args=[date_string])

#         else:
#             date_picker_form = DatePickerForm()
        
#         # return HttpResponseRedirect('this_is_not_my_url')
        
#         return redirect(reverse('date_view', args=[date_string]))
#         # return HttpResponseRedirect(reverse('date_view', args=[date_string]))

# class DateView(View):
#     template_name = 'visits/visits_by_date.html'
#     form_class = DatePickerForm

#     def get(self, request, *args, **kwargs):
#         # queryset = DatePicker.objects
#         # date_picker = get_object_or_404(queryset, id=id)
#         return render(
#             request,
#             'visits/visits_by_date.html',
#             {
#                 'date_picker_form': DatePickerForm()
#             },
#         )