from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from accounts.forms import SignUpForm
from django.views.generic import TemplateView
 

class HomePageView(TemplateView):
    template_name = 'home.html'