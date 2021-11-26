"""gpasite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from basesite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('academics', views.academics, name='academics'),
    path('labs', views.labs, name='labs'),
    path('committee', views.committee, name='committee'),
    path('gallery', views.gallery, name='gallery'),
    path('hostel', views.hostel, name='hostel'),
    path('placements', views.placements, name='placements'),
    path('alumni', views.alumni, name='alumni'),
    path('library', views.library, name='library'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
