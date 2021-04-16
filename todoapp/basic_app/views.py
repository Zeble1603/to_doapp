from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, DeleteView,ListView
from .models import Task
from .forms import TaskForm
# Create your views


class TaskListView(ListView):
    model = Task
    template_name = "home.html"
    
    def get_queryset(self):
        return Task.objects.filter(published_date__lte=timezone.now()).order_by("-due_date")


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    redirect_field_name = 'basic_app/home.html'
    


