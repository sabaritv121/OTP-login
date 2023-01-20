import random

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from otp_app.mixins import MessaHandler


# Create your views here.
from otp_app.models import Profile


def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        profile=Profile.objects.filter(phone_number = phone_number)
        if not profile.exists():
            return redirect("register")
        profile[0].otp = random.randint(1000,9999)
        profile[0].save()
        message_handler = MessaHandler(phone_number,profile[0].otp).send_otp_on_phone()
        return redirect(f'/otp/{profile[0].uid}')
    return render(request,"login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        user= User.objects.create(username=username)
        profile = Profile.objects.create(user=user,phone_number=phone_number)
        return redirect("login_view")
    return render(request,"register.html")


def dashboard(request):
    return render(request,'dashboard.html')


def otp(request,uid):
    return render(request,"otp.html")