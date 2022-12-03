'''views for reports app'''
from datetime import timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from visits.mixins import sum_all_miles
from visits.forms import DatePickerForm
from visits.models import Journey, DatePicker
from users.mixins import MyLoginReqMixin
from .forms import ReportingPeriodForm


class ReportView(MyLoginReqMixin, View):
    '''
    In get displys date picker to pick start date and end date
    of the report
    In post makes query for data from journeys model
    '''

    def get(self, request):
        '''
        gets page that displays two datepickers one for start
        date and the other for end date
        '''
        reporting_period_form = ReportingPeriodForm()
        context = {
            'reporting_period_form': reporting_period_form
        }
        return render(request, 'reports/reporting_period_form.html', context)

    def post(self, request):
        '''
        posts dates and filters data to be displayed in the table
        '''
        # gets data posted by the html form
        form = ReportingPeriodForm(data=request.POST)
        if form.is_valid():
            user_id = request.user.id
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # how many days is the queried period in days
            # as python datetime object
            period_datetime = end_date - start_date
            period_integer_of_days = period_datetime.days

            # query contains all data that I will need for this report
            # I query the database once, than filter results to display
            # in the context

            # need to order by datetime - when created
            query = (
                Journey.objects
                .filter(date_of_journey__range=[start_date, end_date])
                .filter(driver=user_id)).order_by('created_on')
            print(
                f'JORUNEY DATE {journey.date_of_journey for journey in query}')
            results_dict = {}
            # two ways of converting date to datetime object
            # from datetime import datetime, timedelta
            # start_date_datetime = start_date.strftime('%Y-%m-%dT%H:%M:%S.%f')
            # end_date_datetime = datetime.combine(end_date, datetime.min.time())

            # loops through each day starting from start_date
            # in range of the lenght of the reporting period chosen
            for each_date in (start_date + timedelta(n) for n in range(period_integer_of_days + 1)):
                # date is the key in the results dictionary
                date_nice_format = each_date.strftime("%d %B %Y")

                for journey in query:
                    # list of journeys in a day contains journey objects
                    list_of_joruneys_in_a_day = []
                    if journey.date_of_journey == each_date:
                        list_of_joruneys_in_a_day.append(journey)
                    # list of postcodes in a day is the value in the results dictionary
                    day_journeys_data = {
                        'postcodes': [],
                        'miles': 0
                    }
                    list_of_postcodes_in_a_day = []
                    all_miles_in_a_day = 0.0
                    # add start address to postcodes - daily travel starts there
                    # add each destination addresses to postcodes
                    # TODO need to test if the start and destination match
                    # - if they create a fluid journey ???
                    if len(list_of_joruneys_in_a_day) > 0:
                        list_of_postcodes_in_a_day.append(list_of_joruneys_in_a_day[0].postcode_start)

                        for one_journey in list_of_joruneys_in_a_day:
                            list_of_postcodes_in_a_day.append(one_journey.postcode_destination)
                            all_miles_in_a_day += float(one_journey.distance)
                    day_journeys_data['miles'] += all_miles_in_a_day
                    day_journeys_data['postcodes'] = list_of_postcodes_in_a_day
                    print(f'DAY JOURNEYs DATA {day_journeys_data}')
                    print(f'ALL MILES IN A DAY {all_miles_in_a_day}')

                results_dict.update({date_nice_format: day_journeys_data})
            print(f'RESULTS DICCTIONARY {results_dict}')

            context = {
                'results_dict': results_dict,
            }
            return render(request, 'reports/table.html', context)
        return render(request, '/')


class DayReport(MyLoginReqMixin, View):
    """
    Displays the list of journeys that the user has made
    on the day and date picker form in case if user
    wants to display a different day
    """
    def get(self, request, slug, *args, **kwargs):
        """
        gets the date picker form and
        gets Journey objects
        takes slug from datepicker view
        """
        date_picker_item = get_object_or_404(DatePicker, slug=slug)
        date_picked = date_picker_item.date_picked
        date_to_string = date_picked.strftime("%d %B %Y")
        driver_id = request.user.id
        journeys = (
            Journey.objects.filter(date_of_journey=date_picked)
            .filter(driver=driver_id)
            .order_by("created_on")
        )
        sum_miles_day = sum_all_miles(date_picked, Journey, driver_id)
        return render(
            request,
            "visits/visits_by_date.html",
            {
                "slug": slug,
                "date_picker_form": DatePickerForm(),
                "journeys": journeys,
                "date_to_string": date_to_string,
                "driver_id": driver_id,
                "sum_miles_day": sum_miles_day,
            },
        )

    def post(self, request, *args, **kwargs):
        '''
        posts data from datepicker form
        '''
        date_picker_form = DatePickerForm(data=request.POST)
        if date_picker_form.is_valid():
            date_picked_instance = date_picker_form.save(commit=False)
            date_picked_instance.save()
            slug = date_picked_instance.slug
            return redirect("visits:day_report", slug)
        else:
            slug = request.POST.get("date_picked")
            return redirect("visits:day_report", slug)