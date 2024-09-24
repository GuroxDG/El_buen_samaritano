from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("Prueba")