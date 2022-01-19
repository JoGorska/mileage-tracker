from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
# FormView
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings


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
                'user_profile_form': UserProfileForm(),
                'google_api_key': settings.GOOGLE_API_KEY
            },
        )

    def post(self, request, *args, **kwargs):

        user_profile_form = UserProfileForm(data=request.POST)
        if user_profile_form.is_valid():

            user_id = request.user.id
            model = User
            user_object = get_object_or_404(User, id=user_id)
            user_profile_form.instance.profile_of_user = user_object
            user_profile_form.instance.has_profile = True

            user_profile = user_profile_form.save(commit=False)
            user_profile.save()
        
        else:
            user_profile_form = UserProfileForm()

        return HttpResponseRedirect('/')


class EditProfile(CreateView):
    '''
    view to register UserProfile once the user has registered
    '''
    template_name = 'users/user_profile.html'
    form_class = UserProfileForm
    success_url = 'home'

    def get(self, request, user_id, *args, **kwargs):
        user_instance = get_object_or_404(User, id=user_id)
        print(user_instance.user_profile)

        return render(
            request,
            'users/user_profile.html',
            {
                'user_profile_form': UserProfileForm(),
                'google_api_key': settings.GOOGLE_API_KEY
            },
        )

    def post(self, request, user_id, *args, **kwargs):

        user_profile_form = UserProfileForm(data=request.POST)
        if user_profile_form.is_valid():

            user_id = request.user.id
            model = User
            user_object = get_object_or_404(User, id=user_id)
            user_profile_form.instance.profile_of_user = user_object
            user_profile_form.instance.has_profile = True

            user_profile = user_profile_form.save(commit=False)
            user_profile.save()
        
        else:
            user_profile_form = UserProfileForm()

        return HttpResponseRedirect('/')

# def edit_profile(request, user_id):
#     form = UserProfileForm()
#     user_instance = get_object_or_404(User, id=user_id)
#     if user_instance.user_profile:
#         print(f'USER HAS A PROFILIE ALREADY{user_instance.user_profile}')
#     else:
#         print(f'I dont have a profile yet')
#     # instance = get_object_or_404(UserProfile, profile_of_user=user_id)
#     if request.method == 'POST':
#         # form = UserProfileForm(request.POST, instance=instance)
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')    
#     else:
#         # form = UserProfileForm(instance=instance)
#         form = UserProfileForm()

#     return render(request, 'users/user_profile.html', {'form': form})