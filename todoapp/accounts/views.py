from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from accounts.forms import SignUpForm
from django.views.generic.edit import CreateView

# Create your views here.

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

