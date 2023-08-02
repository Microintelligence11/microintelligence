from django.shortcuts import render, redirect
from .models import contactUs
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def thank_you(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        textarea = request.POST['textarea']
        if len(name)<= 3:
            messages.error(request, "Name is too short, please try again later!")
            return redirect('error')
        if len(email)<=11:
            messages.error(request, "email not valid please try agin later!") 
            return redirect('error')
        if len(phone)<10:
            messages.error(request,"phone number not valid, please try again later!")
            return redirect('error')
        if len(textarea)<=5:
            messages.error(request,"please describe your full quary, and try again later!")  
            return redirect('error')

        else:
            contact_Us = contactUs(name=name, email=email, phone=phone, textarea=textarea)
            contact_Us.save()
            messages.success(request,"Your quary has been submitted Successfully.")
    
    return render(request, 'thank_you.html')      
        



def error(request):
    return render(request, 'error.html')
    
