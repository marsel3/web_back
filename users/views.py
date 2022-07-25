from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'web/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'web/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('authorization')