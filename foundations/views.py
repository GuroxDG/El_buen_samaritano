from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from foundations.models import *
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView 
from django.urls import reverse_lazy 
from .forms import *
import csv

#Create your views here.
def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("Prueba")

def descargar_donations(request, id=None):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="donatios.csv"'

    writer = csv.writer(response)

    if id:
        writer.writerow(['id Fundación', 'Fecha de la donación', 'Valor'])
        donaciones = Donation.objects.filter(id=id)
    else:
        writer.writerow(['id Fundación', 'id Usuario', 'Fecha de la donación', 'Valor']) 
        donaciones = Donation.objects.all()

    for donacion in donaciones:
        if id:
            writer.writerow([donacion.id_foundation, donacion.donation_date, donacion.value])
        else:
            writer.writerow([donacion.id_foundation, donacion.id_user, donacion.donation_date, donacion.value])

    return response

class FoundationListView(ListView): 
    model = Foundation 
class FoundationDetailView(DetailView): 
    model = Foundation 
class FoundationCreate(CreateView): 
    model = Foundation 
    form_class = FoundationForm
    
class FoundationUpdate(UpdateView): 
    model = Foundation 
    fields = '__all__' 
class Foundationelete(DeleteView): 
    model = Foundation 
    success_url = reverse_lazy('Foundation-list') 

class UserListView(ListView): 
    model = User 
class UserDetailView(DetailView): 
    model = User 
class UserUpdate(UpdateView): 
    model = User 
    fields = '__all__' 
class UserCreate(CreateView): 
    model = User 
    form_class = UserForm
    
class UserDelete(DeleteView): 
    model = User 
    success_url = reverse_lazy('User-list') 

class DonationListView(ListView): 
    model = Donation 
    
class DonationDetailView(DetailView): 
    model = Donation 

class DonationUpdate(UpdateView): 
    model = Donation 
    fields = '__all__' 

class DonationCreate(CreateView): 
    model = Donation 
    form_class = DonationForm

class DonationDelete(DeleteView): 
    model = Donation 
    success_url = reverse_lazy('Donation-list') 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if True:
        #if form.is_valid():
            #messages.success(request, "Acceso Correcto!")
            return redirect('home') 
        else:
            messages.error(request, "Documento o contraseña inválido.")
    else:
        form = LoginForm()

    return render(request, 'foundations/login.html', {'form': form})

def home_view(request):
    return render(request, 'foundations/home.html') 