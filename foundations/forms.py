import re
import hashlib
from django import forms
from foundations.models import *
from datetime import datetime

def es_numero_positivo(valor):
    return bool(re.match(r'^\d+(\.\d+)?$', str(valor)))

def es_fecha_superior(fecha):
    fecha_actual = datetime.now().date()
    return fecha > fecha_actual

class FoundationFormUpdate(forms.ModelForm):
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

    def clean_nit(self):
        nit = self.cleaned_data.get('nit')
        if Foundation.objects.filter(nit=nit).exists():            
            raise forms.ValidationError("Ya existe una fundación asociada con este nit")
        return nit
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Foundation.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una fundación registrada con este correo")
        return email

class FoundationFormUpdate(forms.ModelForm):
    class Meta:
        model = Foundation
        fields = ['name', 'desc','is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'customCheckbox1'}),
        }
    
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

    def clean_nit(self):
        nit = self.cleaned_data.get('nit')
        if Foundation.objects.filter(nit=nit).exists():            
            raise forms.ValidationError("Ya existe una fundación asociada con este nit")
        return nit
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Foundation.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una fundación registrada con este correo")
        return email
    
class UserFormUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un Usuario registrado con este correo")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password

    
        
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

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if not es_numero_positivo(value):
             raise forms.ValidationError("El valor suministrado de la donación debe ser positivo y superior a cero")
        return value
        
class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
            try:
                user = User.objects.get(email=email, password=password_md5)
            except User.DoesNotExist:
                raise forms.ValidationError("Correo o contraseña incorrectos.")
        return cleaned_data

        
    class Meta:
        model = User
        fields = '__all__' 
        widgets = {
            'document': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
