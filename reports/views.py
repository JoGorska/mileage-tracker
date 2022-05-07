'''views for reports app'''
# pylint: disable=no-member
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from visits.models import Journey


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
        return render(request, 'reports/dates.html')

    def post(self, request):
        '''
        posts dates and filters data to be displayed in the table
        '''
        # gets data posted by the html form
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user_id = request.POST.get('user_id')
        # gets user object
        user = get_object_or_404(User, id=user_id)

        # filter visits by:
        # - user
        # - dates
        all_journeys_in_period = (
            Journey.objects
            .filter(date_of_journey__range=[start_date, end_date])
            .filter(driver=user))
        print(f'JORUNEY DATE {journey.date_of_journey for journey in all_journeys_in_period}')

        # dictionary: date: list of journeys
        # plus I need all mileage of the day

# https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python

        for date in range(start_date, end_date):
            all_journeys_in_one_day = Journey.objects.filter(date).filter(driver=user)
            # I am making a list with postcode start of the first visit
            # and all postcode destinations for all other visits
            list_of_postcodes = [all_journeys_in_one_day[0].postcode_start]
            for journey in all_journeys_in_one_day:
                list_of_postcodes.append(journey.postcode_destination)
        print(f'ALL POSTCODES FOR ONE DAY {list_of_postcodes}')
                
        context = {
            'all_journeys_in_period': all_journeys_in_period,
        }
        return render(request, 'reports/table.html', context)
