from django.contrib import admin
from .models import DatePicker


@admin.register(DatePicker)
class DateAdmin(admin.ModelAdmin):
    list_display = ('date_picked', )
