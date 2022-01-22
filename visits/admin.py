from django.contrib import admin
from .models import Journey, DatePicker


@admin.register(DatePicker)
class DateAdmin(admin.ModelAdmin):

    list_display = ('date_picked', 'slug', )


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):

    list_display = (
                    'id',
                    'date_of_journey',
                    'address_start',
                    'address_destination',
                    )
    readonly_fields = ['id', 'created_on', 'updated_on']
