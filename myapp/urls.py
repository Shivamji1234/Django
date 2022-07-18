from os import name
from django.contrib import admin
from django.urls import path ,include
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('about',views.service,name="service"),
    path('contact',views.contact,name="contact"),
    path('login',views.log,name="login"),
    path('registration1',views.Rig,name="registration"),
    path('feedback',views.feed,name="feedback"),
    path('manali',views.manali,name="manali"),
    path('logout',views.out,name="logout"),
]