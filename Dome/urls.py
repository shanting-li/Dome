"""Dome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Dome import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Index.as_view(),name='index'),
    path('index_1', views.Index_1.as_view(), name='index_1'),
    # path('index_2', views.Index_2.as_view(), name='index_2'),

    path('index_logo/', views.Index_logo.as_view(), name='index_logo'),
    path('index_3/', views.Index_3.as_view(), name='index_3'),

    path('index_forge/', views.Index_forge.as_view(), name='index_forge'),
    path('index_4/', views.Index_4.as_view(), name='index_4')
]
