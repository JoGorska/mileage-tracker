from datetime import datetime
from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, FormView
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


from .models import Journey, DatePicker
from .forms import JourneyForm, DatePickerForm
from .mixins import Directions, extract_postcode
from traffic.models import TrafficMessage


def drive(request):
    """
    Basic view for adding start and destination
    created by following 
    https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
    """
    model = TrafficMessage
    trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    template_name = 'drive.html'
    is_paginated = True
    paginate_by = 6

    context = {
        "trafficmessage_list": trafficmessage_list,
        "paginate_by": paginate_by,
        "is_paginated": is_paginated,
        "google_api_key": settings.GOOGLE_API_KEY
        }
    return render(request, 'visits/drive.html', context)


def drive_next_journey(request, address_destination):
    """
    view that is used for the driver to continue the journey
    without inputing the start address again
    """
    model = TrafficMessage
    trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    is_paginated = True
    paginate_by = 6
    template_name = 'drive.html'
    context = {
        "trafficmessage_list": trafficmessage_list,
        "paginate_by": paginate_by,
        "is_paginated": is_paginated,
        "address_destination": address_destination,
        "google_api_key": settings.GOOGLE_API_KEY
        }
    return render(request, 'visits/drive.html', context)
    # return redirect('visits:drive', context)

def map_view(request):
    """
    Basic view for displaying a map
    created by following (link below)
    https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
    and adjusted to the need of the project
    """

    form = JourneyForm()
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
        "form": form,

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


def map_view_next_journey(request, address_destination):
    """
    view to display map if user was redirected from 
    drive_next_journey view it duplicates the above ???
    """

    form = JourneyForm()
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
        "form": form,

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


class AddJourney(CreateView):
    '''
    need to change the name to ADDJoruney without breaking the view???
    '''
    template_name = 'map.html'
    form_class = JourneyForm()


    def post(self, request, address_start, address_destination, distance, *args, **kwargs):

        form = JourneyForm(data=request.POST)
        if form.is_valid():

            driver_id = request.user.id

            date_of_journey = request.POST.get("date_of_journey")

            address_start = address_start
            postcode_start = extract_postcode(address_start)
            latitude_start = request.POST.get("latitude_start")
            longitude_start = request.POST.get("longitude_start")
            address_destination = address_destination
            postcode_destination = extract_postcode(address_destination)
            latitude_destination = request.POST.get("latitude_destination")
            longitude_destination = request.POST.get("longitude_destination")
            distance = distance

            Journey.objects.create(
                date_of_journey=date_of_journey,
                driver_id=driver_id,
                address_start=address_start,
                postcode_start=postcode_start,
                latitude_start=latitude_start,
                longitude_start=longitude_start,
                address_destination=address_destination,
                postcode_destination=postcode_destination,
                latitude_destination=latitude_destination,
                longitude_destination=longitude_destination,
                distance=distance
            )

        else:
            form = JourneyForm()

        return redirect('visits:next_journey', address_destination)


class DatePickerView(View):
    '''
    Date picker that allows the user to choose which day to display
    successfull url redirects to the page where url contains date
    '''
    template_name = 'visits/date_picker.html'
    form_class = DatePickerForm

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'visits/date_picker.html',
            {
                'date_picker_form': DatePickerForm()
            },
        )

    def post(self, request, *args, **kwargs):
        
        date_picker_form = DatePickerForm(data=request.POST)

        if date_picker_form.is_valid():

            date_picked_instance = date_picker_form.save(commit=False)
            date_picked_instance.save()
            slug = date_picked_instance.slug

            return redirect('visits:date_view', slug )
        # it would be nice to add error handling...???
        # right now else assumes that the date in date picker was a date
        # that was already in the database
        else:
            slug = request.POST.get('date_picked')

            return redirect('visits:date_view', slug )

# class DateView(generic.ListView):
#     '''
#     gets the list of all visits

#     '''
#     model = Journey
#     # need .filter(date_of_journey=slug).
#     queryset = Journey.objects.order_by('created_on')
#     template_name = 'visits/visits_by_date.html'




class DateView(View):
    '''
    Displays the list of journeys that the user has made
    on the day and date picker form in case if user
    wants to display a different day
    '''
    def get(self, request, slug, *args, **kwargs):
        '''
        gets the date picker form and
        gets Journey objects
        takes slug from datepicker view
        '''
        template_name = 'visits/visits_by_date.html'
        form_class = DatePickerForm
        date_picker_item = get_object_or_404(DatePicker, slug=slug)

        date_picked = date_picker_item.date_picked
        date_to_string = date_picked.strftime("%d %B %Y")

        model = Journey

        journeys = Journey.objects.filter(date_of_journey=date_picked).order_by('created_on')

        driver_id = request.user.id

        return render(
            request,
            'visits/visits_by_date.html',
            {
                'date_picker_form': DatePickerForm(),
                'journeys': journeys,
                'date_to_string': date_to_string,
                'driver_id': driver_id
            },
        )


