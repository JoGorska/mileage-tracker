from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, FormView
from .models import TrafficMessage
from .forms import TrafficMessageForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class TrafficMessagesList(generic.ListView):
    model = TrafficMessage
    queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    # for traffic_msg in queryset:
    #     print(F'TRAFFIC MESSAGE THANKS {traffic_msg.thanks.all}')
    template_name = 'index.html'
    paginate_by = 6




# class TrafficMessagesList(generic.ListView):
#     def get(self, request, *args, **kwargs):
#         model = TrafficMessage
#         queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
#         template_name = 'index.html'
#         paginate_by = 6
#         user_request = self.request.GET.get("user.id")
#         print(f'USER REQUEST {user_request}')

#         # attempt to make tanks change colors
#         for traffic_msg in queryset:
#             traffic_message_object = get_object_or_404(queryset, id=traffic_msg.id)
#             thanked = False
#             # if traffic_message_object.thanks.filter(id=user_request.id).exists():
#             #     thanked = True
#         return super(TrafficMessagesList,self).get(request, *args, **kwargs)





# class TrafficMessagesList(CreateView):
#     def get(self, request, *args, **kwargs):
#         model = TrafficMessage
#         trafficmessage_list = TrafficMessage.objects.filter(status=1).order_by('-created_on')
#         template_name = 'index.html'
#         paginate_by = 6
#         user_id = request.user.id
#         # attempt to make tanks change colors
#         for traffic_msg in trafficmessage_list:
#             traffic_message_object = get_object_or_404(trafficmessage_list, id=traffic_msg.id)
#             thanked = False
#             if traffic_message_object.thanks.filter(id=request.user.id).exists():
#                 thanked = True
#         return render(
#             request,
#             'index.html',
#             {
#                 'trafficmessage_list': trafficmessage_list,
#                 'thanked': thanked
#             },
#         )





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

        return HttpResponseRedirect('/')

