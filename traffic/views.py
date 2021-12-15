from django.shortcuts import render
from django.views import generic
from .models import TrafficMessage


class PostMessages(generic.ListView):
    model = TrafficMessage
    queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4
