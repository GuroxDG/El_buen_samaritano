"""
URL configuration for friendsfundation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from foundations import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foundation',views.FoundationListView.as_view(), name='foundation-list'),
    path('foundation/<int:pk>/detail/', views.FoundationDetailView.as_view(), name='foundation-detail'),
    path('foundation/create/', views.FoundationCreate.as_view(), name='foundation-create'),
    
    path('user',views.UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/detail/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    
    path('donation',views.DonationListView.as_view(), name='donation-list'),
    path('donation/<int:pk>/detail/', views.DonationDetailView.as_view(), name='donation-detail'),
    path('donation/create/', views.DonationCreate.as_view(), name='donation-create'),
    
    path('login/', views.login_view, name='login'),
    path('', lambda request: redirect('login'), name='home'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),  # Ruta de logout

]
