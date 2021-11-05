from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.models import User
from .forms import RegistrationForm

class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm 