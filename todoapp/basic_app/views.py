from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, DeleteView,ListView,UpdateView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model

# Create your views
User = get_user_model()

class TaskListView(LoginRequiredMixin,ListView,SelectRelatedMixin):
    model = Task
    template_name = "home.html"
    select_related = ('user','task')
    
    def get_queryset(self):
        return Task.objects.filter(created_date__lte=timezone.now()).order_by("due_date")

class TaskCreateView(LoginRequiredMixin,CreateView,SelectRelatedMixin):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    redirect_field_name = 'basic_app/home.html'
    success_url = reverse_lazy('basic_app:home')
    select_related = ('user','task')

class TaskDeleteView(LoginRequiredMixin,DeleteView,SelectRelatedMixin):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy('basic_app:home')
    select_related = ('user','task')
    
class TaskUpdateView(LoginRequiredMixin,UpdateView,SelectRelatedMixin):
    model = Task
    login_url = "/login/"
    template_name = "task_update.html"
    redirect_field_name = 'basic_app/home.html'
    success_url = reverse_lazy('basic_app:home')
    form_class = TaskForm
    select_related = ('user','task')

    

    


