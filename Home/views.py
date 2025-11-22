from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact
# Create your views here.
def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def contact(request):
     if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         password = request.POST.get('password')
         contact = Contact(name=name, email=email, password=password,  date=datetime.today())
         contact.save()
     return render(request, "contact.html")