from django import forms 
from .models import Company

class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('created_on', 'is_verified', 'user')

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('created_on', 'is_verified', 'name', 'cac', 'user')
