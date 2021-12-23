from django.db import models
from django.db.models import Model
from django.utils.text import slugify
import datetime

# Create your models here.


class DatePicker(models.Model):
    date_picked = models.DateField()
    date_slug = models.SlugField(max_length=255, unique=True)

    # slugify the field function from:
    # https://kodnito.com/posts/slugify-urls-django/

    def save(self, *args, **kwargs):
        
        if not self.date_slug:
            self.date_slug = datetime.strptime(self.date_picked, "%Y-%m-%d")
        super(DatePicker, self).save(*args, **kwargs)
