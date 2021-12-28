from django import forms
from .models import Journey
from .models import DatePicker


class JourneyForm(forms.ModelForm):

    class Meta:
        model = Journey
        fields = (
            'date_of_journey',
            # 'created_on',
            # 'updated_on',

            # 'address_start',

            # 'postcode_start',
            # 'latitude_start',
            # 'longitude_start',

            # 'address_destination',
            # 'postcode_destination',
            # 'latitude_destination',
            # 'longitude_destination',

            # 'driver',

            # 'distance',
        )


class DateInput(forms.DateInput):
    input_type = 'date'


class DatePickerForm(forms.ModelForm):
    class Meta:
        model = DatePicker
        # important - don't forget coma at the end of the list of fields
        fields = ('date_picked', )
        widgets = {
            'date_picked': DateInput(),
        }
