'''forms for reports app'''
import datetime
from django import forms


class DateInput(forms.DateInput):
    '''
    class that ads input_type date to to the widget
    '''
    input_type = 'date'


class ReportingPeriodForm(forms.Form):
    '''
    form that renders start date and end date of the report
    '''
    start_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'col-12 col-lg-6',
                   'id': 'start_date'})

    )
    end_date = forms.DateField(initial=datetime.date.today)


# date field django docs
# https://docs.djangoproject.com/en/3.2/ref/forms/fields/#datefield