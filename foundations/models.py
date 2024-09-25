from django.db import models

# Create your models here.
class Foundations(models.Model):
    nit = models.PositiveBigIntegerField(verbose_name='nit')
    name = models.TextField(max_length=50, verbose_name='nombre')
    email = models.EmailField(verbose_name='correo')
    desc = models.TextField(max_length=100, verbose_name='desc') 
    logo = models.ImageField(upload_to="logos", null=False, blank=True, verbose_name="logo")
    is_active = models.BooleanField(verbose_name='active')

    def __str__(self) -> str:
        return self.name

class TypesDocument(models.Model):
    code = models.CharField(max_length=5, null=False)
    desc = models.TextField(max_length=20, null=False)

    def __str__(self) -> str:
        return f'{self.code} - {self.desc}'

class Users(models.Model):
    type_document = models.CharField(max_length=5, verbose_name='tipo_documento')
    document = models.TextField(max_length=20, verbose_name='documento')
    name = models.TextField(max_length=30, verbose_name='nombre')
    lastname = models.TextField(max_length=30, verbose_name='apellido')
    email = models.EmailField(verbose_name='correo')
    birthday = models.DateField(verbose_name='cumpleaños')
    enterprise = models.TextField(max_length=30, verbose_name='empresa')
    is_friend = models.BooleanField(null=False, verbose_name='amigo')
    id_couple = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    
    def __str__(self) -> str:
        return self.name

class Donations(models.Model):
    id_foundation = models.ForeignKey(Foundations, on_delete=models.CASCADE, related_name='foundations')
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.id_foundation} - {self.id_user}'
