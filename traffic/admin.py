from django.contrib import admin
from .models import TrafficMessage


@admin.register(TrafficMessage)
class MessageAdmin(admin.ModelAdmin):
    '''
    class enabling admin see the model with details and search fields
    '''
    list_display = ('id', 'area', 'county', 'category', 'created_on', 'status')
    search_fields = ['area', 'content']
    list_filter = ('status', 'created_on')
