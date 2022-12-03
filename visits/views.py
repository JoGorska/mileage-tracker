
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views import View
from django.conf import settings
from django.contrib import messages
from users.mixins import MyLoginReqMixin
from traffic.models import TrafficMessage
from .models import Journey, DatePicker
from .forms import JourneyForm, DatePickerForm
from .mixins import Directions, extract_postcode, sum_all_miles


class Drive(MyLoginReqMixin, CreateView):
    '''
    displays the drive.html template with form to submit new journey,
    list of journeys for the day and 3 most recent traffic alerts
    '''
    def get(self, request, slug, *args, **kwargs):
        trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by(
            "-created_on"
        )
        driver_id = request.user.id

        date_picker_item = get_object_or_404(DatePicker, slug=slug)
        date_of_journey = date_picker_item.date_picked
        date_to_string = date_of_journey.strftime("%d %B %Y")
        journeys = (
            Journey.objects.filter(date_of_journey=date_of_journey)
            .filter(driver=driver_id)
            .order_by("created_on")
        )
        sum_miles_day = sum_all_miles(date_of_journey, Journey, driver_id)
        context = {
            "date_of_journey": date_of_journey,
            "date_to_string": date_to_string,
            "slug": slug,
            "driver_id": driver_id,
            "journeys": journeys,
            "trafficmessage_list": trafficmessage_list,
            "sum_miles_day": sum_miles_day,
            "google_api_key": settings.GOOGLE_API_KEY,
        }
        return render(request, "visits/drive.html", context)


class AddJourney(MyLoginReqMixin, CreateView):
    """
    when form is being posted the latitude and longditude is collected
    from the the form and passed to Directions functions
    which fetches data from google directions api
    I need to create instance of the form, than validate it
    if the form valid I can fetch directions
    than I can save the data in the database
    """

    template_name = "drive.html"

    def post(self, request, slug, *args, **kwargs):
        """
        fills in instance of JourneyForm with data posted by the form,
        if form is valid fetches directions data from google maps
        than saves a new instance of Journey object to database
        """

        form = JourneyForm(request.POST or None, request.FILES or None)
        trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by(
            "-created_on"
        )

        if form.is_valid():
            latitude_start = request.POST.get("latitude_start")
            longitude_start = request.POST.get("longitude_start")
            latitude_destination = request.POST.get("latitude_destination")
            longitude_destination = request.POST.get("longitude_destination")
            directions = Directions(
                lat_a=latitude_start,
                long_a=longitude_start,
                lat_b=latitude_destination,
                long_b=longitude_destination,
            )

            address_start_google_directions = directions["origin"]
            address_start = request.POST.get("address_start")
            address_destination_google_directions = directions["destination"]
            address_destination = request.POST.get("address_destination")
            date_picker_item = get_object_or_404(DatePicker, slug=slug)
            date_of_journey = date_picker_item.date_picked
            date_to_string = date_of_journey.strftime("%d %B %Y")
            driver_id = request.user.id
            journeys = (
                Journey.objects.filter(date_of_journey=date_of_journey)
                .filter(driver=driver_id)
                .order_by("created_on")
            )

            postcode_start = extract_postcode(
                address_start, address_start_google_directions
            )
            postcode_destination = extract_postcode(
                address_destination, address_destination_google_directions
            )
            distance = directions["distance"]

            current_journey = Journey.objects.create(
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
                distance=distance,
            )
            sum_miles_day = sum_all_miles(date_of_journey, Journey, driver_id)
            context = {
                "sum_miles_day": sum_miles_day,
                "current_journey": current_journey,
                "date_picker_form": DatePickerForm(),
                "journeys": journeys,
                "trafficmessage_list": trafficmessage_list,
                "date_to_string": date_to_string,
                "driver_id": driver_id,
                "slug": slug,
                "google_api_key": settings.GOOGLE_API_KEY,
            }
            return render(request, "visits/drive.html", context)

        else:
            # this block handles when the form fails form validation
            form_errors = form.errors
            form_as_data = form.errors.as_data()
            list_of_fields_with_errors = form_as_data.keys()

            # seperate message for errors caused by missing geocoordinates
            if (
                ("latitude_start" in list_of_fields_with_errors) or (
                 "longitude_start" in list_of_fields_with_errors) or (
                 "latitude_destination" in list_of_fields_with_errors) or (
                 "longitude_destination" in list_of_fields_with_errors)):

                messages.error(
                    request,
                    "We couldn't collect geocoordinates for the"
                    " address. Please make sure you click into"
                    " the drop down list after typing the address."
                    " If the drop down field doesnt apear,"
                    "reload the browser. Please be aware that some"
                    " browsers' extensions will stop the drop down"
                    " from showing.",
                )

            else:
                # this captures any other errors that might apear
                messages.error(request, form_errors)

            date_picker_item = get_object_or_404(DatePicker, slug=slug)
            date_of_journey = date_picker_item.date_picked
            date_to_string = date_of_journey.strftime("%d %B %Y")
            driver_id = request.user.id
            journeys = (
                Journey.objects.filter(date_of_journey=date_of_journey)
                .filter(driver=driver_id)
                .order_by("created_on")
            )

            context = {
                "journeys": journeys,
                "trafficmessage_list": trafficmessage_list,
                "date_to_string": date_to_string,
                "form": JourneyForm(),
                "slug": slug,
                "google_api_key": settings.GOOGLE_API_KEY,
            }
            return render(request, "visits/drive.html", context)


class EditJourney(MyLoginReqMixin, CreateView):
    """
    gets the drive.html pre filled and posts the journey form
    """

    def get(self, request, slug, journey_id, *args, **kwargs):
        """
        displays drive.html template filled with data from journey.id
        """
        driver_id = request.user.id

        date_picker_item = get_object_or_404(DatePicker, slug=slug)
        date_of_journey = date_picker_item.date_picked
        date_to_string = date_of_journey.strftime("%d %B %Y")
        journeys = (
            Journey.objects.filter(date_of_journey=date_of_journey)
            .filter(driver=driver_id)
            .order_by("created_on")
        )
        edited_journey = get_object_or_404(Journey, id=journey_id)
        trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by(
            "-created_on"
        )
        sum_miles_day = sum_all_miles(date_of_journey, Journey, driver_id)

        context = {
            "edited_journey": edited_journey,
            "date_of_journey": date_of_journey,
            "date_to_string": date_to_string,
            "slug": slug,
            "journey_id": journey_id,
            "driver_id": driver_id,
            "journeys": journeys,
            "trafficmessage_list": trafficmessage_list,
            "sum_miles_day": sum_miles_day,
            "google_api_key": settings.GOOGLE_API_KEY,
        }
        return render(request, "visits/drive.html", context)

    def post(self, request, slug, journey_id, *args, **kwargs):
        """
        fills in instance of JourneyForm with data posted by the form,
        if form is valid fetches directions data from google directions
        than saves a new instance of Journey object to database
        """

        form = JourneyForm(request.POST or None, request.FILES or None)
        trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by(
            "-created_on"
        )

        if form.is_valid():
            latitude_start = request.POST.get("latitude_start")
            longitude_start = request.POST.get("longitude_start")
            latitude_destination = request.POST.get("latitude_destination")
            longitude_destination = request.POST.get("longitude_destination")
            directions = Directions(
                lat_a=latitude_start,
                long_a=longitude_start,
                lat_b=latitude_destination,
                long_b=longitude_destination,
            )

            address_start_google_directions = directions["origin"]
            address_start = request.POST.get("address_start")
            address_destination_google_directions = directions["destination"]
            address_destination = request.POST.get("address_destination")
            date_picker_item = get_object_or_404(DatePicker, slug=slug)
            date_of_journey = date_picker_item.date_picked
            date_to_string = date_of_journey.strftime("%d %B %Y")
            driver_id = request.user.id
            journeys = (
                Journey.objects.filter(date_of_journey=date_of_journey)
                .filter(driver=driver_id)
                .order_by("created_on")
            )

            postcode_start = extract_postcode(
                address_start, address_start_google_directions
            )
            postcode_destination = extract_postcode(
                address_destination, address_destination_google_directions
            )
            distance = directions["distance"]
            edited_journey = get_object_or_404(Journey, id=journey_id)

            edited_journey.address_start = address_start
            edited_journey.postcode_start = postcode_start
            edited_journey.latitude_start = latitude_start
            edited_journey.longitude_start = longitude_start
            edited_journey.address_destination = address_destination
            edited_journey.postcode_destination = postcode_destination
            edited_journey.latitude_destination = latitude_destination
            edited_journey.longitude_destination = longitude_destination
            edited_journey.distance = distance

            edited_journey.save(
                update_fields=[
                    "address_start",
                    "postcode_start",
                    "latitude_start",
                    "longitude_start",
                    "address_destination",
                    "postcode_destination",
                    "latitude_destination",
                    "longitude_destination",
                    "distance",
                ]
            )

            return redirect("reports:day_report", slug)

        else:
            # this block handles when the form fails form validation
            form_errors = form.errors
            form_as_data = form.errors.as_data()
            list_of_fields_with_errors = form_as_data.keys()

            # seperate message for errors caused by missing geocoordinates
            if ((
                "latitude_start" in list_of_fields_with_errors) or (
                "longitude_start" in list_of_fields_with_errors) or (
                "latitude_destination" in list_of_fields_with_errors) or (
                    "longitude_destination" in list_of_fields_with_errors)):

                messages.error(
                    request,
                    "We couldn't collect geocoordinates for the"
                    " address. Please make sure you click into"
                    " the drop down list after typing the address."
                    " If the drop down field doesnt apear,"
                    "reload the browser. Please be aware that some"
                    " browsers' extensions will stop the drop down"
                    " from showing.",
                )

            else:
                # this captures any other errors that might apear
                messages.error(request, form_errors)

            date_picker_item = get_object_or_404(DatePicker, slug=slug)
            date_of_journey = date_picker_item.date_picked
            date_to_string = date_of_journey.strftime("%d %B %Y")
            driver_id = request.user.id
            journeys = (
                Journey.objects.filter(date_of_journey=date_of_journey)
                .filter(driver=driver_id)
                .order_by("created_on")
            )

            context = {
                "journeys": journeys,
                "trafficmessage_list": trafficmessage_list,
                "date_to_string": date_to_string,
                "form": JourneyForm(),
                "slug": slug,
                "google_api_key": settings.GOOGLE_API_KEY,
            }
            return render(request, "visits/drive.html", context)


def delete_journey(request, slug, journey_id):
    '''
    deletes the journey from the database
    '''
    journey = get_object_or_404(Journey, id=journey_id)
    journey.delete()
    return redirect("reports:day_report", slug)



class DatePickerDrive(MyLoginReqMixin, View):
    """
    view that posts the data from the date picker form
    and transfers the user to vie drive_date_ready
    with pre-filled date and url reflecting the date
    """
    template_name = "visits/date_picker.html"
    form_class = DatePickerForm

    def get(self, request, *args, **kwargs):
        '''
        gets date picker form
        '''
        return render(
            request,
            "visits/date_picker.html",
            {"date_picker_form": DatePickerForm()},
        )

    def post(self, request, *args, **kwargs):
        '''
        posts date picker form data
        '''
        date_picker_form = DatePickerForm(data=request.POST)
        if date_picker_form.is_valid():
            date_picked_instance = date_picker_form.save(commit=False)
            date_picked_instance.save()
            slug = date_picked_instance.slug
            return redirect("visits:drive_date_ready", slug)
        else:
            slug = request.POST.get("date_picked")

            return redirect("visits:drive_date_ready", slug)
