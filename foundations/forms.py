from django import forms
from foundations.models import *
from datetime import datetime

def es_fecha_superior(fecha):
    fecha_actual = datetime.now().date()
    return fecha > fecha_actual

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
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 
        widgets = {
            'type_document': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
            'document': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control datetimepicker-input','type': 'date'}),
            'enterprise': forms.TextInput(attrs={'class': 'form-control'}),
            'is_friend': forms.CheckboxInput(attrs={'class': 'customCheckbox1'}),
            'id_couple': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
            'id_rol': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible'}),
        }

    def clean_document(self):
        document = self.cleaned_data.get('document')
        if User.objects.filter(document=document).exists():            
            raise forms.ValidationError("Ya existe un Usuario asociado a este documento")
        return document
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un Usuario registrado con este correo")
        return email
    
    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if es_fecha_superior(birthday):
             raise forms.ValidationError("La fecha suministrada supera la fecha de registro")
        return birthday
        
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
