import hashlib
from django.db import models
from django.urls import reverse
from django.core.validators import *
from django.core.exceptions import *
from django.contrib import messages


#Create your models here.
class Rol(models.Model):
    name = models.TextField(max_length=50, verbose_name='nombre')
    description = models.TextField(verbose_name='descripcion')

    def __str__(self) -> str:
        return self.name

class Foundation(models.Model):
    nit = models.PositiveBigIntegerField(verbose_name='nit', unique=True)
    name = models.TextField(max_length=50, verbose_name='nombre')
    email = models.EmailField(verbose_name='correo', validators=[EmailValidator()])
    desc = models.TextField(max_length=100, verbose_name='descripcion') 
    logo = models.ImageField(upload_to="media/logos/")
    is_active = models.BooleanField(verbose_name='activo', default=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('foundation-list')

class TypesDocument(models.Model):
    code = models.CharField(max_length=5, null=False)
    desc = models.TextField(max_length=50, null=False)

    def __str__(self) -> str:
        return f'{self.code} - {self.desc}'

class User(models.Model):
    email = models.EmailField(verbose_name='correo', unique=True)
    password = models.TextField(max_length=200, verbose_name='Contraseña') 

    def save(self, *args, **kwargs):
        self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
    
    def get_absolute_url(self):
        return reverse('user-list')

class Donation(models.Model):
    id_foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE, related_name='foundation')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    donation_date  = models.DateField(verbose_name='Fecha Donación', auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.id_foundation} - {self.id_user}'
    
    def get_absolute_url(self):
        return reverse('donation-list')
