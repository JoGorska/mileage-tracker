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
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

# this might fix issue with index.html not seeing that user is authenticated

# from django.contrib.auth import authenticate, login as auth_login
# function based view for custom user model

# def add_user(request):
# if request.method == 'POST':
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = User.objects.get(email=form.cleaned_data['email'])
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 auth_login(request, user)
#                 return HttpResponseRedirect(request.GET.get('next',
#                                             settings.LOGIN_REDIRECT_URL))
#         else:
#             error = 'Invalid username or password.'