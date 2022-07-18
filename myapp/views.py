from contextlib import nullcontext
import email
from  myapp.models import feedback
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from pkg_resources import NullProvider
from django.shortcuts import redirect, render
from django.http import HttpResponse
import random
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return HttpResponse("this is about page")
def contact(request):
    return render(request,"contact.html")
def service(request):
    return HttpResponse("this is about page")
def out(request):
    logout(request)
    messages.success(request,"you are logout")
    return render(request,"login.html")
    
def log(request):
    if request.method =='POST':
        username=request.POST['username']  
        password1=request.POST['password1']
        User=authenticate(username=username,password=password1)
        if User is not None:
            login(request,User)
            first_name =User.first_name
            
            return render(request,"home.html",{'first_name':first_name})
        else:
            messages.error(request,"you are not register")
            return render(request,"login.html")
    else:    
        return render(request,'login.html')

    
def  feed(request):
    if( request.method == 'POST'):
      name=request.POST['name']
      email=request.POST['email']
      details=request.POST['details']
      so=feedback(name=name,email=email, details=details,date=datetime.today())
      so.save()
      messages.success(request, 'Your feedback is Submited."Thanks for your feedback".')
    
    return render(request,"feedback.html")
    

def  Rig(request):
    if( request.method == 'POST'):
        Username=request.POST['username']  
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_id=request.POST['email_id']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            
                myuser=User.objects.create_user(Username,email_id,password1)
                myuser.first_name=first_name
                myuser.last_name=last_name
                myuser.save()
                messages.success(request, 'Your are now Registered."Thanks for your Registration".')
                return render(request,"login.html")
        else:
              messages.error(request, 'Your are not Registered.')
              return render(request,"registration1.html")
    else:
        return render(request,"registration1.html")


    

            
def manali(request):
    return render(request,"manali.html")
    
    