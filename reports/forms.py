'''forms for reports app'''
import datetime
from django import forms
from django.conf import settings


class ReportingPeriodForm(forms.Form):
    '''
    form that renders start date and end date of the report
    '''
    start_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            format=settings.DATE_INPUT_FORMATS,
            attrs={'class': 'mt-2'}),
    )
    end_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        initial=datetime.date.today,
        widget=forms.DateInput(
            format=settings.DATE_INPUT_FORMATS,
            attrs={'class': 'mt-2'}))

    def clean_start_date(self):
        '''
        returns errors if the field is filled in incorrectly
        '''
        self.cleaned_data['start_date']
        if data != None and data > datetime.now():
            raise forms.ValidationError(
                    """
                    \'to\' date cannot be later than today.
                    """)
# clean the data