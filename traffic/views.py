from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import TrafficMessage


class TrafficMessagesList(generic.ListView):
    model = TrafficMessage
    queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    # attempt to add functionality to add thanks and cleared

    # def get(self, request, id, *args, **kwargs):
    #     queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    #     trafficmessage = get_object_or_404(queryset, id=id)
    #     thanks = False
    #     cleared = False
    #     if trafficmessage.thanks.filter(id=self.request.user.id).exists():
    #         thanks = True
    #     if trafficmessage.cleared.filter(id=self.request.user.id).exists():
    #         cleared = True
        
    #     return render(
    #         request,
    #         "index.html",
    #         {
    #             "trafficmessage": trafficmessage,
    #             "thanks": thanks,
    #             "cleared": cleared
    #         },
    #     )
