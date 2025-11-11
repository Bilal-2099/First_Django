from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable0": "This is sent from views.py",
        "variable1": "Greetings, welcome to our website!",
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is services page")
def contact(request):
    return HttpResponse("This is contact page")