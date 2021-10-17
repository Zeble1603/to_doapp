from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    name = models.CharField(max_length=150,blank=False)
    due_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def get_absolute_url(self):
        return reverse('home', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


        
    