from django.contrib import auth
# Create your models here.

class User(auth.models.User):
    def __str__(self):
        return self.username

