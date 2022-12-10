'''views for reports app'''
from datetime import timedelta, datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse

from visits.mixins import sum_all_miles
from visits.forms import DatePickerForm
from visits.models import Journey, DatePicker
from users.mixins import MyLoginReqMixin
from .forms import ReportingPeriodForm
from .exporter import ExcellExporter, get_mileage_headers


class ReportingOptionsView(MyLoginReqMixin, TemplateView):
    template_name = 'reports/reporting_options.html'


class ChoosePeriodView(MyLoginReqMixin, View):
    '''
    In get displys date picker to pick start date and end date
    of the report
    In post makes query for data from journeys model
    '''
    def get_success_url(self, request, start_date, end_date):
        return redirect('reports:period_report', start_date=start_date, end_date=end_date)

    def get(self, request):
        '''
        gets page that displays two datepickers one for start
        date and the other for end date
        '''
        form = ReportingPeriodForm()
        context = {
            'reporting_period_form': form
        }
        return render(request, 'reports/reporting_period_form.html', context)

    def post(self, request):
        '''
        posts dates and filters data to be displayed in the table
        '''
        # gets data posted by the html form
        form = ReportingPeriodForm(data=request.POST)
        if form.is_valid():
            start_date = str(form.cleaned_data['start_date'])
            end_date = str(form.cleaned_data['end_date'])
            # how many days is the queried period in days
            # as python datetime object
            return self.get_success_url(request, start_date, end_date)
        context = {
            'reporting_period_form': form
        }
        return render(request, 'reports/reporting_period_form.html', context)


class PeriodExcelView(ChoosePeriodView):
    def get_success_url(self, request, start_date, end_date):
        return redirect('reports:excel_report', start_date=start_date, end_date=end_date)


class PeriodReportView(MyLoginReqMixin, View):

    def get_all_day_data(self, all_journeys):
        dates = [journey.date_of_journey for journey in all_journeys]
        all_days_dict_list = []
        for date in dates:
            this_day_dict = {}
            this_day_journey_objects = []
            this_day_postcodes = []
            this_day_distance = 0
            for journey in all_journeys:
                if journey.date_of_journey == date:
                    this_day_journey_objects.append(journey)
                    this_day_postcodes.append(journey.postcode_destination)
                    this_day_distance += journey.distance
            this_day_postcodes.insert(0, this_day_journey_objects[0].postcode_start)
            postcodes = str(this_day_postcodes)
            bracket = postcodes.replace('[', '')
            other_bracket = bracket.replace(']', '')
            final = other_bracket.replace("'", '')
            this_day_dict = {
                'date': date.strftime('%d.%m.%Y'),
                'postcodes': final,
                'distance': this_day_distance,
            }
            all_days_dict_list.append(this_day_dict)
        return all_days_dict_list

    def get(self, request, **kwargs):
        template_name = 'reports/table.html'
        start_date_str = kwargs['start_date']
        end_date_str = kwargs['end_date']
        all_journeys = Journey.objects.filter(date_of_journey__range=[start_date_str, end_date_str])
        journeys_dicts = self.get_all_day_data(all_journeys)
        context = {

            'journeys': journeys_dicts,
            'start_date': start_date_str,
            'end_date': end_date_str,
        }
        return render(request, template_name, context)


class excelExportJourneys(MyLoginReqMixin, View):

    def get(self, request, **kwargs):
        start_date_str = kwargs['start_date']
        end_date_str = kwargs['end_date']
        all_journeys = Journey.objects.filter(date_of_journey__range=[start_date_str, end_date_str])
        journeys_dicts = PeriodReportView.get_all_day_data(self, all_journeys=all_journeys)
        headers = get_mileage_headers()
        excel = ExcellExporter(queryset=journeys_dicts, export_object='mileage', headers=headers)
        return excel.export_worksheet()


class DatePickerView(MyLoginReqMixin, View):
    '''
    Date picker that allows the user to choose which day to display
    successfull url redirects to the page where url contains date
    '''
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
            return redirect("reports:day_report", slug)
        else:
            slug = request.POST.get("date_picked")
            return redirect("reports:day_report", slug)


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
            return redirect("reports:day_report", slug)
        else:
            slug = request.POST.get("date_picked")
            return redirect("reports:day_report", slug)