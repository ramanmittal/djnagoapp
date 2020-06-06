from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST.get("username") 
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are succesfully logged in.")
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid Login Attempt.")
    return render(request,"accounts/login.html")
def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name") 
        last_name=request.POST.get("last_name") 
        username=request.POST.get("username") 
        email=request.POST.get("email") 
        password=request.POST.get("password") 
        password2=request.POST.get("password2")
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exist.")
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exist.")
            user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,"You are registered successfully.")
            return redirect("login")
        else:
            messages.error(request,"Password don't match.") 
    return render(request,"accounts/register.html")
def dashboard(request):
    usercontacts=Contact.objects.order_by("-contact_date").filter(user_id=request.user.id)
    return render(request,"accounts/dashboard.html",{"usercontacts":usercontacts})
def logout(request):
    messages.success(request,"You are logged out successfully.")
    auth.logout(request)
    return redirect('index')
