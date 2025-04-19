from django import forms 
from .models import Resume

class AddResumeForm(forms.ModelForm):
    class Meta:
        model = Resume 
        exclude = ('user', 'created_on')

class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume 
        exclude = ('user', 'created_on')