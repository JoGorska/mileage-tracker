'''forms for reports app'''
import datetime
from django import forms
from django.conf import settings


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
            attrs={'class': 'mt-2', 'type': 'date'}))
    end_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'mt-2', 'type': 'date'}))


class PickDateForm(forms.Form):
    '''
    form that renders one input for date of the report
    '''
    date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'mt-2', 'type': 'date'}))

