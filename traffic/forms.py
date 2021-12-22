from .models import TrafficMessage
from django import forms


class TrafficMessageForm(forms.ModelForm):
    class Meta:
        model = TrafficMessage
        # important - don't forget coma at the end of the list of fields
        fields = ('area', 'county', 'content', 'category', )