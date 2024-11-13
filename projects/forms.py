from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'area']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Título del proyecto'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción del proyecto'})
        }