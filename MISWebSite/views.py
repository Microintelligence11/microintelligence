from django.shortcuts import render, redirect
from .models import contactUs, BookOnline
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def book_online(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        service_name = request.POST['service_name']
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
        if len(city)<= 3:
                messages.error(request, "Cityn ame is too short, please try again later!")
                return redirect('error')
        if service_name == "select":
             messages.error(request, "Please select Service & try again later!")
             return redirect('error')
        else:
             book_online = BookOnline(name=name, email=email, phone=phone, city=city, service_name=service_name, textarea=textarea)
             book_online.save()
             messages.success(request,"your service book successfully, we are connect you shortly.")
             return redirect('thank_you')

    return render(request, 'book_online.html')

def contact(request):
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
                return redirect('thank_you')
            
        return render(request, 'contact.html')


def thank_you(request):
    return render(request, 'thank_you.html')      
        

def error(request):
    return render(request, 'error.html')

def view_software_development(request):
     return render(request, 'view_software_development.html')

def view_web_development(request):
     return render(request, 'view_web_development.html')

def view_app_development(request):
     return render(request, 'view_app_development.html')

def view_blog_development(request):
     return render(request, 'view_blog_development.html')

def view_landing_page_development(request):
     return render(request, 'view_landing_page_development.html')

def view_digital_marketing(request):
     return render(request, 'view_digital_marketing.html')

def view_seo(request):
     return render(request, 'view_seo.html')

def view_facebook_ads(request):
     return render(request, 'view_facebook_ads.html')

def view_google_ads(request):
     return render(request, 'view_google_ads.html')

def view_web_hosting(request):
     return render(request, 'view_web_hosting.html')


def terms_and_conditions(request):
     return render(request,'terms_and_conditions.html')

def privacy_policy(request):
     return render(request,'privacy_policy.html')

def sitemap(request):
     return render(request, 'sitemap.xml')
    

