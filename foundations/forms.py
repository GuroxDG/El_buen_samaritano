from django import forms
from foundations.models import *

class FoundationForm(forms.ModelForm):
    class Meta:
        model = Foundation
        fields = '__all__' 
        widgets = {
            'nit': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            #'logo': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'customCheckbox1'}),
        }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 
        widgets = {
            'document': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'enterprise': forms.TextInput(attrs={'class': 'form-control'}),
            'is_friend': forms.CheckboxInput(attrs={'class': 'customCheckbox1'}),
        }
        
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__' 
        widgets = {
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
        }