"""
URL configuration for crms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crmsapp import views


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('ainsert/', views.insert),
    path('show/', views.list),
    path('cinsert/', views.cinsert),
    path('clist/', views.clist),
    path('<id>/carupdate/', views.update_car_view),
    path('alogin/',views.alogin),
    path('ahome/',views.ahome),
    path('register/',views.register),
    path('addcar/',views.addcar),
    path('carlist/',views.carlist),
    path('adminlogin/',views.admin_login),
    path('ulogin/',views.user_login),
    path('alistcar/',views.alistcar),
    path('adelete_car/<int:id>',views.adelete_car),
    path('findcar/',views.findcar),
    path('findcark/',views.predict),
    path('predictcar/',views.predictwithinput),
    path('predictcarfrompprice/',views.predictcarfrompprice),
]
