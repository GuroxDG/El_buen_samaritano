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
            'type_document': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
            'document': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control datetimepicker-input'}),
            'enterprise': forms.TextInput(attrs={'class': 'form-control'}),
            'is_friend': forms.CheckboxInput(attrs={'class': 'customCheckbox1'}),
            'id_couple': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
            'id_rol': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
        }
        
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__' 
        widgets = {
            'donation_date': forms.DateInput(attrs={'class': 'form-control datetimepicker-input'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_user': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
            'id_foundation': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
        }
        
class LoginForm(forms.Form):
    document = forms.CharField(max_length=50, label='Documento')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    def clean(self):
        cleaned_data = super().clean()
        document = cleaned_data.get('document')
        password = cleaned_data.get('password')

        if document and password:
            password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()

            try:
                user = User.objects.get(document=document, password=password_md5)
            except User.DoesNotExist:
                raise forms.ValidationError("Documento o contraseña incorrecta.")
            
            return cleaned_data
        
    class Meta:
        model = User
        fields = '__all__' 
        widgets = {
            'document': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
