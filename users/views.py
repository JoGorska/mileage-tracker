from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
# FormView
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from .forms import (
    UserForm,
    UserProfileForm,
    )


class RegisterUserView(CreateView):
    '''
    class view to register user as a build in User model from django
    '''
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = reverse_lazy('users:user_profile')

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                )
        login(self.request, new_user)
        return HttpResponseRedirect(self.success_url)


class UserProfile(CreateView):
    '''
    view to register UserProfile once the user has registered
    '''
    template_name = 'users/user_profile.html'
    form_class = UserProfileForm
    success_url = 'home'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'users/user_profile.html',
            {
                'user_profile_form': UserProfileForm()
            },
        )

    def post(self, request, *args, **kwargs):

        user_profile_form = UserProfileForm(data=request.POST)
        # print(f'REQUEST {request.get.user.id}')
        if user_profile_form.is_valid():

            user_id = request.user.id
            print(f'BLOODY USER NEEDS TO BE ALREADY LOGGED IN{user_id}')
            model = User
            user_object = get_object_or_404(User, id=user_id)
            user_profile_form.instance.profile_of_user = user_object
            # user_profile_form.instance.profile_of_user = request.POST.get("user_id")
            user_profile_form.instance.has_profile = True

            user_profile = user_profile_form.save(commit=False)
            user_profile.save()
        
        else:
            user_profile_form = UserProfileForm()

        return HttpResponseRedirect('/')