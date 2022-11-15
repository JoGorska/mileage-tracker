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

    # class Meta:
    #     fields = ('start_date', 'end_date',)
    #     widgets = {
    #         'date_picked': DateInput(),
    #     }
    # def clean_start_date(self):
    #     '''
    #     returns errors if the field is filled in incorrectly
    #     '''
    #     data = self.cleaned_data['start_date']
    #     if data > datetime.datetime.today:
    #         raise forms.ValidationError(
    #             """
    #             \'to\' date cannot be later than today.
    #             """)
# clean the data
