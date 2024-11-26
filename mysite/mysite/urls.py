"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from prueba import views  # Importa las vistas desde tu aplicación llamada "prueba"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list, name='user_list.html'),  # Configura la URL para listar usuarios
    path('', views.login, name='login.html'),
    path('control/', views.control_list, name='control_list.html' ),
]
