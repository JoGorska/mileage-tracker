from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect

from .models import DatePicker
from .forms import DatePickerForm


class DateView(View):
    template_name = 'visits/visits_by_date.html'
    form_class = DatePickerForm
    success_url = 'date_picker'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'visits/visits_by_date.html',
            {
                'date_picker_form': DatePickerForm()
            },
        )

    def post(self, request, *args, **kwargs):
        date_picker_form = DatePickerForm(data=request.POST)

        # do I need to check if date is already in database or 
        # will the slug do the job???
        # queryset = DatePicker.objects.order_by('date_slug')
        # date_picked = get_object_or_404(queryset, date_slug=date_slug)

        # if date_picked.date_slug.exists():
        #     return HttpResponseRedirect('date_picker')

        # else:

        if date_picker_form.is_valid():
            # date_picker_form.instance.date_picked = date_picked
            # date_picker_form.instance.date_slug = date_slug
            date_picked = date_picker_form.save(commit=False)
            date_picked.save()
        else:
            date_picker_form = DatePickerForm()
        
        return HttpResponseRedirect('date_picker')

