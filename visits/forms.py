from django import forms
from .models import DatePicker


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
