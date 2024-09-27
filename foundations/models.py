from django.db import models
from django.urls import reverse

# Create your models here.
class Foundation(models.Model):
    nit = models.PositiveBigIntegerField(verbose_name='nit')
    name = models.TextField(max_length=50, verbose_name='nombre')
    email = models.EmailField(verbose_name='correo')
    desc = models.TextField(max_length=100, verbose_name='desc') 
    logo = models.ImageField(upload_to="media/logos/")
    is_active = models.BooleanField(verbose_name='active')

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
    type_document = models.ForeignKey(TypesDocument, on_delete=models.CASCADE, null=True, related_name='TipoDocumento')
    document = models.TextField(max_length=20, verbose_name='documento')
    name = models.TextField(max_length=30, verbose_name='nombre')
    lastname = models.TextField(max_length=30, verbose_name='apellido')
    email = models.EmailField(verbose_name='correo')
    birthday = models.DateField(verbose_name='cumpleaños')
    enterprise = models.TextField(max_length=30, verbose_name='empresa')
    is_friend = models.BooleanField(null=False, verbose_name='amigo')
    id_couple = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    is_active = models.BooleanField(verbose_name='active')
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('user-list')

class Donation(models.Model):
    id_foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE, related_name='foundation')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    donation_date  = models.DateField(verbose_name='FechaDonacion')
    
    def __str__(self) -> str:
        return f'{self.id_foundation} - {self.id_user}'
    
    def get_absolute_url(self):
        return reverse('donation-list')
