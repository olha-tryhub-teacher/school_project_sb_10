from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView



class ProfileDetailView(DetailView):
    model = User
    template_name = "tasks/profile.html"

class CustomLoginView(LoginView):
    template_name = "tasks/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = "tasks:login"


class RegisterView(CreateView):
    template_name = "tasks/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("tasks:login"))
