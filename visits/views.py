from datetime import datetime
from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import DatePicker
from .forms import DatePickerForm


class DatePickerView(View):
    template_name = 'visits/date_picker.html'
    form_class = DatePickerForm

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'visits/date_picker.html',
            {
                'date_picker_form': DatePickerForm()
            },
        )

    def post(self, request, *args, **kwargs):

        date_picker_form = DatePickerForm(data=request.POST)


        if date_picker_form.is_valid():

            date_picked_record = date_picker_form.save(commit=False)
            date_picked_record.save('date_picked')
            date_picked = request.POST.get('date_picked')
            print(date_picked_record)

            # date_only = datetime.date(date_picked)
            date_string = str(date_picked)

            print(date_string)
            # date_to_string = date_picked.strftime("%Y-%m-%d")
            # date_object = datetime.strptime(date_picked, "%Y-%m-%d")
            # date_to_string = str(date_object)
            # print(date_to_string)
            # only_date = date_to_string.split(" ")
            

            # only_date = date_to_string[:-9]
            # print(only_date)
            # return reverse('date_view', args=[date_to_string])
            

        else:
            date_picker_form = DatePickerForm()
        
        return HttpResponseRedirect('this_is_not_my_url')
        
        # return HttpResponseRedirect(reverse('date_view', args=[date_to_string]))

class DateView(View):
    template_name = 'visits/visits_by_date.html'
    form_class = DatePickerForm

    def get(self, request, *args, **kwargs):
        # queryset = DatePicker.objects
        # date_picker = get_object_or_404(queryset, id=id)
        return render(
            request,
            'visits/visits_by_date.html',
            {
                'date_picker_form': DatePickerForm()
            },
        )