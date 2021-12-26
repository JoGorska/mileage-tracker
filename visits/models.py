import random
import string

from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User


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
