from django import forms
from .models import Journey
from .models import DatePicker


class JourneyForm(forms.ModelForm):
    


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
