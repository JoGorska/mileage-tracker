from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import TrafficMessage
from .forms import TrafficMessageForm
from django.urls import reverse_lazy


class TrafficMessagesList(generic.ListView):
    model = TrafficMessage
    queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class TrafficMsgDetail(View):

    def get(self, request, id, *args, **kwargs):
        # model = TrafficMessage
        queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
        trafficmessage = get_object_or_404(queryset, id=id)
        thanks = False
        cleared = False
        if trafficmessage.thanks.filter(id=self.request.user.id).exists():
            thanks = True
        if trafficmessage.cleared.filter(id=self.request.user.id).exists():
            cleared = True

        return render(
            request,
            "traffic_msg_detail.html",
            {
                "trafficmessage": trafficmessage,
                "thanks": thanks,
                "cleared": cleared
            },
        )


class AddNewTrafficMsg(CreateView):
    model = TrafficMessage
    form_class = TrafficMessageForm
    template_name = 'add_traffic_msg.html'

    def post(self, request, id, *args, **kwargs):
        queryset = User.objects.filter


        # user = get_object_or_404(queryset, id=id)
        # user_id = user.id
        # return render (
        #     request,
        #     "add_traffic_msg.html",

        # )

# class AddNewTrafficMsg(CreateView):
#     template_name = 'add_traffic_msg.html'
#     form_class = TrafficMessageForm
#     success_url = reverse_lazy('/')

#     def form_valid(self, form):
#         form.save()
#         return HttpResponseRedirect(self.success_url)
