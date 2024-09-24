from django.urls import path
from .views import my_test_view

urlpatterns = [
    path("listado/", my_test_view),
]
