"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from pathlib import Path
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path ,include

admin.site.site_header = "Shivam Admin"
admin.site.index_title = "Welcome to Shivam protal"
admin.site.site_title = "Shivam protal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myapp.urls")),
    path('home',include("myapp.urls")),
    path('about',include("myapp.urls")),
    path('contact',include("myapp.urls")),
    path('service',include("myapp.urls")),
    path('login',include("myapp.urls")),
    path('feedback',include("myapp.urls")),
    path('manali',include("myapp.urls")),
    path('registration1',include("myapp.urls"))
    
]
