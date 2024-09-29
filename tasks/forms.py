from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'detalles', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control ', 'required': 'required'}),
            'detalles': forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }
