'''forms for visits app'''
from django import forms
from .models import Journey
from .models import DatePicker


class DateInput(forms.DateInput):
    '''
    class that ads input_type date to to the widget
    '''
    input_type = 'date'


class JourneyForm(forms.ModelForm):
    '''
    form to input the date of the journey on the map view,
    the rest of data needed for Journey model are taken from the
    variables that are already on map page
    '''

    class Meta:
        '''
        class meta points to the model, Journey, which form will reffer to and 
        specifies the fields off the model that need to be rendered 
        '''
        model = Journey
        fields = (
            'address_start',
            'latitude_start',
            'longitude_start',
            'address_destination',
            'latitude_destination',
            'longitude_destination',

        )


class DatePickerForm(forms.ModelForm):
    '''
    form to pick a date for a list of journeys to be displayed
    '''
    class Meta:
        '''
        Form refers to model datepicker and renders date_picked field
        with widget DateInput
        '''
        model = DatePicker
        fields = ('date_picked', )
        widgets = {
            'date_picked': DateInput(),
        }
