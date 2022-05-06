from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from visits.models import Journey

# Create your views here.


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
        print(f'JORUNEY DATE {journey.date for journey in all_journeys_in_period}')
        context = {
            'all_journeys_in_period': all_journeys_in_period,
        }
        return render(request, 'reports/table.html', context)
