from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=150,blank=False)
    due_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("home", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


        
    