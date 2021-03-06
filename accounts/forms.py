from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()
    
    def __init__(self,*args,**kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'

