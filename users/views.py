from django.shortcuts import render
from django.views.generic.edit import CreateView
# FormView
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import (
    UserForm,
    # UserProfileForm,
    # AuthForm,
    )


class RegisterUserView(CreateView):
    template_name = 'register/register.html'
    form_class = UserForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

