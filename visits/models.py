import random
import string

from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User


class Journey(models.Model):

    date_of_journey = models.DateField(verbose_name="Date of the Journey", unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    address_start = models.CharField(verbose_name="Start (full address)", max_length=100, null=True, blank=True)
    # postcode is the end of the string of address before UK ???
    postcode_start = models.CharField(verbose_name="Start Postcode", max_length=100, null=True, blank=True)
    latitude_start = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    longitude_start= models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)

    address_destination = models.CharField(verbose_name="Destination (full address)", max_length=100, null=True, blank=True)
    postcode_destination = models.CharField(verbose_name="Destination Postcode", max_length=100, null=True, blank=True)
    latitude_destination = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    longitude_destination = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)

    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits", null=True, blank=True)

    distance = models.DecimalField(verbose_name="Distance Travelled", max_digits=19, decimal_places=10, null=True, blank=True)


class DatePicker(models.Model):
    date_picked = models.DateField(unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            date_string = str(self.date_picked)

            self.slug = date_string
        super(DatePicker, self).save(*args, **kwargs)
