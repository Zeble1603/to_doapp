from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('name','due_date')

    def __init__(self,*args,**kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class':'input is-link','type':'text','placeholder':'Your task'})
        
        


