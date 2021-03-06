'''forms for traffic message app'''
from .models import TrafficMessage
from django import forms


class TrafficMessageForm(forms.ModelForm):
    '''
    form to create new traffic alerts
    '''
    class Meta:
        '''
        metadata for traffic message form
        '''
        model = TrafficMessage
        # important - don't forget coma at the end of the list of fields
        fields = ('area', 'county', 'content', 'category', )
