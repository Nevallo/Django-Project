from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')


def about(request):
    return render(request,"MainApp/about.html")

def registration(request):
    return render(request, "MainApp/registration.html")
    return redirect("home")