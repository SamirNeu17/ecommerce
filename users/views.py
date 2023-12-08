from django.shortcuts import render,redirect
from django.http import HttpResponse
import users.forms as forms
from users.models import User, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

#Create your views here.

def index(request):
    return render(request,"index.html")

def user_login(request):
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        check_user = User.objects.filter(email=email)
        if check_user.exists() is False:
            error_message="Email  does not exist"
            messages.error(request,error_message)
            return redirect ("login")
    username= check_user[0].username
    valid_user = authenticate(username=username,password=password)
    if valid_user:
        login(request,valid_user)
        return redirect("profile")
    else:
        error_message ="Invalid email or password"
        message.error(request,error_message)
        return redirect("login")
    return render(request,"login.html")

def register(request):
    
    return render (request,"register.html")


def register(request):
    register_form = forms.RegisterForm()
    context= {"form": register_form}
    return render (request,"register.html",context)



def user_profile(request):
    return render (request,"profile.html")


