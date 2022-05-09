'''views for reports app'''
# pylint: disable=no-member
from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from visits.models import Journey
from .forms import ReportingPeriodForm


class ReportView(View):
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
            start_date_datetime = start_date.strftime('%Y-%m-%dT%H:%M:%S.%f')
            end_date_datetime = datetime.combine(end_date, datetime.min.time())

            # loops through each day starting from start_date
            # in range of the lenght of the reporting period chosen
            for each_date in (start_date + timedelta(n) for n in range(period_integer_of_days + 1)):
                print(f'DATE {each_date}')
                for journey in query:
                    list_of_joruneys_in_a_day = []

                    if journey.date_of_journey == each_date:
                        list_of_joruneys_in_a_day.append(journey)
                    list_of_postcodes_in_a_day = []
                    # add start address to postcodes
                    # add all destination addresses to postcodes
                    # need to test if the start and destination match - if they create a fluid journey ???
                    if len(list_of_joruneys_in_a_day) > 0:
                        list_of_postcodes_in_a_day.append(list_of_joruneys_in_a_day[0].postcode_start)
                        print(f'SHOULD BE ONE POSTCODE {list_of_postcodes_in_a_day}')
                        for one_journey in list_of_joruneys_in_a_day:
                            list_of_postcodes_in_a_day.append(one_journey.postcode_destination)
                        print(f'should be long list of postcodes {list_of_postcodes_in_a_day}')
                results_dict.update({each_date: list_of_postcodes_in_a_day})
            print(f'RESULTS DICCTIONARY {results_dict}')

                        


#         # dictionary:
#         # date: list of journeys = keys
#         # plus I need all mileage of the day = values = []

# # https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python

#         for date in range(start_date, end_date):
#             all_journeys_in_one_day = Journey.objects.filter(date).filter(driver=user)
#             # I am making a list with postcode start of the first visit
#             # and all postcode destinations for all other visits
#             list_of_postcodes = [all_journeys_in_one_day[0].postcode_start]
#             for journey in all_journeys_in_one_day:
#                 list_of_postcodes.append(journey.postcode_destination)
#         print(f'ALL POSTCODES FOR ONE DAY {list_of_postcodes}')
                
            # context = {
            #     'all_journeys_in_period': all_journeys_in_period,
            # }
            return render(request, 'reports/table.html')
        return render(request, '/')
