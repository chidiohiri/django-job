from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job 
        exclude = ('company', 'user', 'created_on', 'expiry_date', 'is_verified')

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job 
        exclude = ('company', 'user', 'created_on', 'expiry_date', 'is_verified')