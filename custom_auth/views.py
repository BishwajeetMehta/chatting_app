from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from . models import User
from django.contrib import messages
from django.utils.dateparse import parse_date
from datetime import date
from django.core.mail import send_mail
import os
from django.contrib.auth import authenticate, login

# Create your views here.
class SignupPageView(TemplateView):
    template_name = "signup.html"

class demo(TemplateView):
    template_name ="demo.html"

class UserView(View):
    def post(self,request):
        data = request.POST
        usertable = User()
        username = data.get("username")
        if not username :
            messages.error(request,"User name cannot be null ")
            return redirect("signupform")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect("signupform")
        usertable.username = username 

        email = data.get("email")
        if not email:
            messages.error(request,"Email cannot be null ")
            return redirect("signupform")
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect("signupform")
        usertable.email = email

        firstname = data.get("firstname")
        if not firstname :
            messages.error(request,"firstname cannot be null ")
            return redirect("signupform")
        usertable.first_name = firstname

        lastname = data.get("lastname")
        if not lastname :
            messages.error(request,"lastname cannot be null ")
            return redirect("signupform")
        usertable.last_name = lastname

        password = data.get("password")
        if not password :
            messages.error(request,"Password cannot be null ")
            return redirect("signupform")
        if len(password) < 8:
            messages.error(request,"Password must be of 8 characters or more ")
            return redirect("signupform")
        confirm_password = data.get("confirm_password")
        if not confirm_password:
            messages.error(request,"confirm Password field cannot be null")
            return redirect("signupform")
        if password != confirm_password:
            messages.error(request,"Password not matched")
            return redirect("signupform")
        usertable.set_password(password)

        phone = data.get("phone")
        if not phone:
            messages.error(request,"Phone Number cannot be null ")
            return redirect("signupform")
        if User.objects.filter(phone=phone).exists():
            messages.error(request,"Phone Number already exists")
            return redirect("signupform")
        usertable.phone =phone 

        DoB = data.get("DoB")
        if not DoB :
            messages.error(request,"Date of Birth cannot be null")
            return redirect("signupform")
        Dob = parse_date(DoB)
        if not Dob:
            messages.error(request, "Invalid Date of Birth format")
            return redirect("signupform")
        today = date.today()
        age = today.year - Dob.year - ((today.month, today.day) < (Dob.month, Dob.day))
        if age < 18:
            messages.error(request,"You must be at least 18 years old to register.")
            return redirect("signupform")
        usertable.DoB = Dob
        gender = data.get("gender")
        if not gender:
            messages.error(request,"Gender field cannot be null")
            return redirect("signupform")
        usertable.gender = gender
        usertable.save()

        #emial logic
        subject = f' Registration Sucessful ! '
        message = f"Dear { usertable.username}, Your Registration is Sucessful !\n \n \n Thank you for choosing Us"
        from_email = os.getenv("EMAIL_HOST")
        recipient_list = [usertable.email]
        send_mail(subject, message, from_email, recipient_list)
        return redirect("login")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        print("post hitted")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            messages.error(request, "Username cannot be null")
            return redirect("login")

        if not password:
            messages.error(request, "Password cannot be null")
            return redirect("login")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("demo")  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
