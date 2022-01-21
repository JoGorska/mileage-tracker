from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import TrafficMessage
from .forms import TrafficMessageForm


class TrafficMessagesList(generic.ListView):
    '''
    class view enabling to display the list of traffic allerts with pagination
    '''
    model = TrafficMessage
    queryset = TrafficMessage.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class AddNewTrafficMsg(CreateView):
    '''
    class view in get - gets the traffic_msg_form and in post - posts the form
    and creates new traffic alert
    '''
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
    '''
    posts thanks when user clicks the button, this ads user to the list of
    users that added thanks to particular traffic alert, if user double clicks
    the thanks get canceled
    '''
    def post(self, request, msg_id):
        traffic_message = get_object_or_404(TrafficMessage, id=msg_id)
        if traffic_message.thanks.filter(id=request.user.id).exists():
            traffic_message.thanks.remove(request.user)
        else:
            traffic_message.thanks.add(request.user)

        return HttpResponseRedirect('/')
