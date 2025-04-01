from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
 
 
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
 
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
     
class LogoutInterfaceView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')  # Redirect to home or any other page
        return HttpResponseForbidden("You are not allowed to perform this action")

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
