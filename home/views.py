from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    return render(request,"projects.html")

def contact(request):
    if request.method=="POST":
        contact=Contact()
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        number=request.POST.get("number")
        message=request.POST.get("message")
        contact.firstname=firstname
        contact.lastname=lastname
        contact.email=email
        contact.number=number
        contact.message=message
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")
        
    return render(request,"contactform.html")

