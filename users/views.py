from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
def user_register(request):
    return render (request,"user_register.html")
