from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django import forms
from django.urls import reverse


def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("notes")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("notes")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("welcome")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['avatar', 'first_name', 'last_name', 'username', 'email']
    template_name = 'profile.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['avatar'].widget = forms.FileInput()
        return form

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})