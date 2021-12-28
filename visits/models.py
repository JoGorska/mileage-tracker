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


# def rand_slug():
#     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class DatePicker(models.Model):
    date_picked = models.DateField(unique=True)
    # driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="date_picker")
    # slug = models.SlugField(max_length=255, unique=True)

    # slugify the field function from:
    # https://kodnito.com/posts/slugify-urls-django/



    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.id + "-" + self.date_picked)
    #     super(DatePicker, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if not self.slug:

    #         # date_to_string = self.date_picked.strptime("%Y-%m-%d")
    #         self.slug = slugify(rand_slug() + "-" + self.date_picked)
    #     super(DatePicker, self).save(*args, **kwargs)



    # def save(self, date_picked, *args, **kwargs):

    #     if not self.date_slug:
    #         self.date_slug = self.date_picked.strptime("%Y-%m-%d")
    #     super(DatePicker, self).save(date_picked, *args, **kwargs)
