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
        model = TrafficMessage
        trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
        current_traffic_msg = get_object_or_404(trafficmessage_list, id=id)
        thanks = False
        cleared = False
        template_name = 'index.html'
        if current_traffic_msg.thanks.filter(id=self.request.user.id).exists():
            thanks = True
        if current_traffic_msg.cleared.filter(id=self.request.user.id).exists():
            cleared = True

        return render(
                request,
                "traffic/traffic_msg_detail.html",
                {
                    "trafficmessage_list": trafficmessage_list,
                    "current_traffic_msg ": current_traffic_msg,
                    "thanks": thanks,
                    "cleared": cleared,
                },
            )


class AddNewTrafficMsg(CreateView):
    template_name = 'traffic/add_traffic_msg.html'
    form_class = TrafficMessageForm
    success_url = 'home'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'traffic/add_traffic_msg.html',
            {
                'traffic_msg_form': TrafficMessageForm()
            },
        )

    def post(self, request, *args, **kwargs):

        traffic_msg_form = TrafficMessageForm(data=request.POST)
        if traffic_msg_form.is_valid():
            traffic_msg_form.instance.author_id = request.user.id

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

        return HttpResponseRedirect('/')


# class MsgCleared(View):
#     def post(self, request, id):
#         traffic_message = get_object_or_404(TrafficMessage, id=id)
#         if traffic_message.cleared(id=request.user.id).exists():
#             traffic_message.cleared.remove(request.user)
#         else:
#             traffic_message.cleared.add(request.user)

#         return HttpResponseRedirect(reverse('traffic/traffic_msg_detail', args=[id]))
