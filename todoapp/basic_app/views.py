from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, DeleteView,ListView,UpdateView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
# Create your views


class TaskListView(ListView):
    model = Task
    template_name = "home.html"
    
    def get_queryset(self):
        return Task.objects.filter(created_date__lte=timezone.now()).order_by("-due_date")

class TaskCreateView(CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    redirect_field_name = 'basic_app/home.html'
    success_url = reverse_lazy('basic_app:home')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy('basic_app:home')
    
class TaskUpdateView(UpdateView):
    model = Task
    login_url = "/login/"
    template_name = "task_update.html"
    redirect_field_name = 'basic_app/home.html'
    success_url = reverse_lazy('basic_app:home')
    form_class = TaskForm


    

    


