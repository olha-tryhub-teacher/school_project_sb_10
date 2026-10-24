from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "profile_user"

    def get_object(self, queryset=None):
        return self.request.user


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("users:profile")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.get_or_create(user=user)
        login(self.request, user)
        return redirect("users:profile")