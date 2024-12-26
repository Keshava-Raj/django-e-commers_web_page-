from django.shortcuts import render, redirect
from .models import Register_form ,create_user
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login


def home(request):
    return render(request,"home.html")


def Login_use(request):
    if request.method == 'GET':
        return render(request, 'Login.html' )

    if request.method == 'POST': 
        email_id = request.POST['email']
        password = request.POST['paswd']
        User = authenticate(request , email=email_id, password=password)
        if User is not None:
            login (request,User)
            #if Register_form.objects.filter(email=email_id) and Register_form.objects.filter(passewrd=password):
            rie = Register_form.objects.all()
            
            messages.success( request, "your succssessfully Login in Your Account")
            
            return redirect("Dashbord")
        else:
            messages.error( request, "you enterd bad credentials")
            return redirect("login")
    return render(request, 'Login.html', {'fname':rie})

def Register_use(request):
    if request.method == 'GET':
        return render(request,"register.html") 
    
    if request.method == 'POST':
        name = request.POST['name2']
        email = request.POST['email2']
        phone = request.POST['phonePR']
        age = request.POST['Age']
        password = request.POST['passd3']
        confirm_password = request.POST['passd2']
        
        if UserManager.objects.filter(email=email):
            messages.error(request ,"This email id is already exist try anather email id")
            return redirect("Regester")
        if UserManager.objects.filter(mobile=phone):
            messages.error(request ,"This Phone number is already exist try anather Phone number")
            return redirect("Regester")
            
        if password != confirm_password:
            messages.error(request ,"Password doe'nt match")
            return redirect("Regester")
        
        myuser = UserManager.objects.create(
                fist_name=name,
                email=email,
                mobile=phone,
                age=age,
                password=password,
        ).save()
        
        messages.success(request,'your Account is succssefully Created')
    
    return redirect( "Dashbord" )

def dashbord_use(request):
    return render(request,'Dashbord.html')


