from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    '''
    Our UserProfile model extends the built-in Django User Model
    This model was created following Bobby did coding tutorial
    on Django and Google API
    https://github.com/bobby-didcoding/did_django_google_api_tutorial/blob/main/users/models.py
    and adjusted to the needs of the project
    '''
    # retalional field in relation to the user

    profile_of_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    # full address of the person
    address = models.CharField(verbose_name="Your Address", max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)
    # details that will be needed for reporting to the employer

    employer_organization = models.CharField(verbose_name="Employer Organization", max_length=200, null=True, blank=True)
    employer_email = models.EmailField(max_length=254, unique=False, null=True, blank=True)
    employee_ref_number = models.CharField(verbose_name="Employee Refference Number", max_length=50, null=False, blank=True)
    
    employer_address = models.CharField(verbose_name="Employer's Main Office", max_length=100, null=True, blank=True)
    employer_longitude = models.CharField(verbose_name="Employer's Longitude", max_length=50, null=True, blank=True)
    employer_latitude = models.CharField(verbose_name="Employer's Latitude", max_length=50, null=True, blank=True)

    # other admin data

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    has_profile = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.profile_of_user}'
