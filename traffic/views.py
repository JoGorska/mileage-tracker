from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, FormView
from .models import TrafficMessage
from .forms import TrafficMessageForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


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
    template_name = 'add_traffic_msg.html'
    form_class = TrafficMessageForm
    success_url = 'home'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_traffic_msg.html',
            {
                'traffic_msg_form': TrafficMessageForm()
            },
        )

    def post(self, request, *args, **kwargs):

        traffic_msg_form = TrafficMessageForm(data=request.POST)
        if traffic_msg_form.is_valid():
            traffic_msg_form.instance.author_id = request.user.id
            traffic_msg_form.instance.status = 1
            traffic_message = traffic_msg_form.save(commit=False)
            traffic_message.save()
        
        else:
            traffic_msg_form = TrafficMessageForm()

        return HttpResponseRedirect('/')


class MsgThanks(View):
    def post(self, request, id):
        traffic_message = get_object_or_404(TrafficMessage, id=id)
        if traffic_message.thanks.filter(id=request.user.id).exists():
            traffic_message.thanks.remove(request.user)
        else:
            traffic_message.thanks.add(request.user)

        return HttpResponseRedirect(reverse('traffic_msg_detail', args=[id]))
