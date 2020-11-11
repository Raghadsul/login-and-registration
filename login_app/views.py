from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name=first_name,last_name=last_name, email=email, password=pw_hash)
    return redirect("/")

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['username'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect('/success')
        return redirect("/")

def index2(request):
    context = { 
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, "index2.html", context)

def logout(request):
    del request.session['userid']
    return redirect("/")
