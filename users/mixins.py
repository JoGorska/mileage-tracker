from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class MyLoginReqMixin(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
