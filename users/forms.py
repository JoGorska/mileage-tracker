from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

# forms were created by following Bobby did coding tutorial on Django and Google API
# https://github.com/bobby-didcoding/did_django_google_api_tutorial/blob/main/users/models.py
# and adjusted to the needs of the project

class UserForm(UserCreationForm):
    '''
    Form that uses built-in UserCreationForm to handel user creation
    '''
    first_name = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(
            attrs={'placeholder': '*Your first name..'}
            )
        )
    last_name = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(
            attrs={'placeholder': '*Your last name..'}
            )
        )
    username = forms.EmailField(
        max_length=254, required=True, widget=forms.TextInput(
            attrs={'placeholder': '*Email..'}
            )
        )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '*Password..', 'class': 'password'}
            )
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '*Confirm Password..', 'class': 'password'}
            )
        )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password1', 'password2',
        )


class UserProfileForm(forms.ModelForm):
    '''
    Basic model-form for our user profile that extends Django user model.

    '''
    address = forms.CharField(max_length=100)
    longitude = forms.CharField(max_length=50)
    latitude = forms.CharField(max_length=50)

    employer_address = forms.CharField(max_length=100)
    employer_longitude = forms.CharField(max_length=50)
    employer_latitude = forms.CharField(max_length=50)

    class Meta:
        model = UserProfile
        fields = (
            'your_address',
            'longitude',
            'latitude',
            'employee_ref_number',

            'employer_organization',
            'employer_email',
            'employer_address',
            'employer_longitude',
            'employer_latitude'

        )
