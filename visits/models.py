import random
import string

from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User


class Journey(models.Model):

    date_of_journey = models.DateField(verbose_name="Date of the Journey", unique=False, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    address_start = models.CharField(verbose_name="Start (full address)", max_length=100, null=False, blank=False)
    address_destination = models.CharField(verbose_name="Destination (full address)", max_length=100, null=False, blank=False)

    latitude_start = models.DecimalField(max_digits=40, decimal_places=20, null=False, blank=False)
    longitude_start= models.DecimalField(max_digits=40, decimal_places=20, null=False, blank=False)
    latitude_destination = models.DecimalField(max_digits=40, decimal_places=20, null=False, blank=False)
    longitude_destination = models.DecimalField(max_digits=40, decimal_places=20, null=False, blank=False)

    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits", null=False, blank=True)
    distance = models.DecimalField(verbose_name="Distance Travelled", max_digits=19, decimal_places=1, null=False, blank=True)
    # postcode is the end of the string of address before UK ???
    postcode_start = models.CharField(verbose_name="Start Postcode", max_length=100, null=False, blank=True)
    postcode_destination = models.CharField(verbose_name="Destination Postcode", max_length=100, null=False, blank=True)

class DatePicker(models.Model):
    date_picked = models.DateField(unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            date_string = str(self.date_picked)

            self.slug = date_string
        super(DatePicker, self).save(*args, **kwargs)
