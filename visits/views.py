import json
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


class Drive(CreateView):
    def get(self, request, slug, *args, **kwargs):
        '''
        gets the view for Drive url after date is submitted
        '''
        model = TrafficMessage
        trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
        template_name = 'drive.html'
        is_paginated = True
        paginate_by = 6

        model = DatePicker
        form_class = DatePickerForm

        driver_id = request.user.id
        
        date_picker_item = get_object_or_404(DatePicker, slug=slug)
        date_of_journey = date_picker_item.date_picked
        context = {
            'date_picker_form': DatePickerForm(),
            'date_of_journey': date_of_journey,
            'driver_id': driver_id,
            'trafficmessage_list': trafficmessage_list,
            'paginate_by': paginate_by,
            'is_paginated': is_paginated,
            'google_api_key': settings.GOOGLE_API_KEY

        }

        return render(request, 'visits/drive.html', context)
 

class AddJourney(CreateView):
    '''
    when form is being posted the latitude and longditude is collected from the form
    and passed to Directions functions which fetches data from google maps/ directions api
    I need to create instance of the form, than validate it
    if the form valid I can fetch directions
    than I can save the data in the database
    '''
    template_name = 'drive.html'
    form_class = JourneyForm()

    form = JourneyForm(data=request.POST)

    def post(self, request, slug, *args, **kwargs):

        form = JourneyForm(data=request.POST)
        print(f'JOURNEY FORM {form}')

        if form.is_valid():
            '''
            I will fetch directions from google after I know the form is valid
            this means that I have my longditude and latitude in place.
            check is journey model requires lat and long???
            '''
            ## this is temporary, I need to get lat and long from form instance!
            # because it was validated!
            lat_a = request.POST.get("lat_a")
            long_a = request.POST.get("long_a")
            lat_b = request.POST.get("lat_b")
            long_b = request.POST.get("long_b")

            directions = Directions(
                lat_a=lat_a,
                long_a=long_a,
                lat_b=lat_b,
                long_b=long_b
                )

            date_picker_item = get_object_or_404(DatePicker, slug=slug)
            # this gives me date object
            date_of_journey = date_picker_item.date_picked
            # date_of_journey = request.datepicker.date_picked
            driver_id = request.user.id

            address_start = directions.origin
            postcode_start = extract_postcode(address_start)
            # latitude_start = form.instance.lat...
            latitude_start = request.POST.get("latitude_start")
            longitude_start = request.POST.get("longitude_start")
            address_destination = directions.destination
            postcode_destination = extract_postcode(address_destination)
            latitude_destination = request.POST.get("latitude_destination")
            longitude_destination = request.POST.get("longitude_destination")
            distance = directions.distance

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
        # this is temporary so I know it works???
        return redirect('visits:date_picker')
        # next_journey is not ready
        # return redirect('visits:next_journey', address_destination)

def drive_next_journey(request, slug, journey_id):
    """
    this function will display the drive.html template
    with additional data passed from Drive view (slug and journey_id)
    """
    # not sure if I need this?
    template_name = 'drive.html'
    # I need DatePicker model to display this chosen date and pass to Journey
    # display Datepicked in the small header
    # fill in the field for journey form from
    # Journey model:
    # I need to get object_or_404 for the journey_id that was passed from Drive
    # this will fill in the accordeon on the header
    # and add coordinates to the map icon

    # I need to filter Journey model to display all journeys for this day
    
    # this is to display the list of traffic alerts down below
    model = TrafficMessage
    trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    is_paginated = True
    paginate_by = 6

    context = {
        "trafficmessage_list": trafficmessage_list,
        "paginate_by": paginate_by,
        "is_paginated": is_paginated,
        "address_destination": address_destination,
        "google_api_key": settings.GOOGLE_API_KEY
        }
    return render(request, 'visits/drive.html', context)


def drive_edit_journey(request, journey_id):
    """
    takes journey_id and pre fills the fields
    with address_start and address_destination
    """
    model = TrafficMessage
    trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    is_paginated = True
    paginate_by = 6

    model = Journey
    journey = get_object_or_404(Journey, id=journey_id)

    template_name = 'drive.html'
    context = {
        "trafficmessage_list": trafficmessage_list,
        "paginate_by": paginate_by,
        "is_paginated": is_paginated,
        "journey": journey,
        "google_api_key": settings.GOOGLE_API_KEY
        }
    return render(request, 'visits/drive.html', context)






class UpdateJourney(CreateView):
    '''
    need to change the name to ADDJoruney without breaking the view???
    '''
    template_name = 'map.html'
    form_class = JourneyForm()


    def post(self, request, journey_id, address_start, address_destination, distance, *args, **kwargs):

        form = JourneyForm(data=request.POST)
        model = Journey()

        journey = get_object_or_404(Journey, id=journey_id)

        # some form validation would be nice???

        journey.address_start = address_start
        journey.postcode_start = extract_postcode(address_start)
        journey.latitude_start = request.POST.get("latitude_start")
        journey.longitude_start = request.POST.get("longitude_start")
        journey.address_destination = address_destination
        journey.postcode_destination = extract_postcode(address_destination)
        journey.latitude_destination = request.POST.get("latitude_destination")
        journey.longitude_destination = request.POST.get("longitude_destination")
        journey.distance = distance

        date_of_journey = journey.date_of_journey
        slug = str(date_of_journey)

        journey.save()

        return redirect('visits:day_report', slug)


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

            return redirect('visits:day_report', slug)
        # it would be nice to add error handling...???
        # right now else assumes that the date in date picker was a date
        # that was already in the database
        else:
            slug = request.POST.get('date_picked')

            return redirect('visits:day_report', slug)

class DatePickerDrive(View):
    '''
    view that posts the data from the date picker form
    and transfers the user to vie drive_date_ready
    with pre-filled date and url reflecting the date
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

            return redirect('visits:drive_date_ready', slug)
        # it would be nice to add error handling...???
        # right now else assumes that the date in date picker was a date
        # that was already in the database
        else:
            slug = request.POST.get('date_picked')

            return redirect('visits:drive_date_ready', slug)

class DayReport(View):
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
        driver_id = request.user.id

        journeys = Journey.objects.filter(date_of_journey=date_picked).filter(driver=driver_id).order_by('created_on')

        

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


