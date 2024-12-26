from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Register_form , Provider_register,Addvaickal,vaik_taking_user
from django.contrib import messages


from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login



 

def basefile(request):
    return render(request, "sbasefile.html")    

def Provide_dashboard(request):
    row1 = Provider_register.objects.all()
    return render(request, "provider dashaboard.html",{"Profile2":row1} ) 
'''
def aisebikes(request):
    
    if request.method == 'GET':
        return render(request, "home.html") 

    if request.method == 'POST':  
        email_id2 = request.POST['email1']
        password2 = request.POST['passwrd1']
        
        User=Provider_register( Register_form.objects.filter(email=email_id2) and Register_form.objects.filter(passewrd=password2))
        if User is None:
            login(request,User)   
            rie = Register_form.objects.all()
            messages.success( request, "your succssessfully Login in Your Account")
            return redirect("dashboard")
            
            
        else:
            messages.error( request, "you enterd bad credentials")
            return redirect("userlogin")
    return render(request, 'user dashbord.html',{'fname':rie} )
'''
def home(request):
    return render(request, "home.html") 

def Aboutus(request):
    
    return render(request, "About us.html")

def contact1(request):
    
    return render(request, "contact Us.html")

def users_register(request):

        return render(request,'test file.html')
    
def dashboard(request):
    # Logic for dashboard view
    return render(request, 'user dashbord.html')

def provider_register(request):
    if request.method == 'GET':
        return render(request,"provider register.html") 
    if request.method == 'POST':
        namep = request.POST['name2']
        username = request.POST['username']
        emailp = request.POST['email2'] 
        phonep = request.POST['phonePR']
        passwordp = request.POST['passd3']
        passwordp2 = request.POST['passd4']
        date_of_birth = request.POST['DOT']
        gender = request.POST['GENDER']
        vaickelnumber = request.POST['vaickel'] 
        provider_img = request.POST['RC']
        
        if Provider_register.objects.filter(email=emailp):
            messages.error(request ,"This email id is already exist try anather email id")
            return redirect("provider")
        if Provider_register.objects.filter(phone_number=phonep):
            messages.error(request ,"This Phone number is already exist try anather Phone number")
            return redirect("provider")
            
        if passwordp != passwordp2:
            messages.error(request ,"Password doe'nt match")
            return redirect("provider") 
        
        provider_R = Provider_register.objects.create(
            name = namep,
            email= emailp,
            Username = username,
            phone_number = phonep,
            password = passwordp,
            passwordR =  passwordp2,
            date_of_birth = date_of_birth,
            gender = gender,
            vekele_number = vaickelnumber,
            image = provider_img,
        ).save()
        messages.success(request,'your Vaickel Provider Account as been succssefully Created')
        return redirect("providerdashboard")
        

def users_register(request):
    if request.method == 'GET':
        return render(request,"test file.html") 
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['mobile']
        age = request.POST['age']
        password = request.POST['paswd']
        confirm_password = request.POST['paswd1']
        
        if Register_form.objects.filter(email=email):
            messages.error(request ,"This email id is already exist try anather email id")
            return redirect("register")
        if Register_form.objects.filter(mobile=phone):
            messages.error(request ,"This Phone number is already exist try anather Phone number")
            return redirect("register")
            
        if password != confirm_password:
            messages.error(request ,"Password doe'nt match")
            return redirect("register")
        
        myuser = Register_form.objects.create(
                name=name,
                email=email,
                mobile=phone,
                age=age,
                passewrd=password,
                passewrd1 = confirm_password
        ).save()
        
        messages.success(request,'your Account is succssefully Created')
    
    return redirect( "userlogin" )


#from django.contrib.auth.hashers import make_password, check_password

def user_login(request):
    if request.method == 'GET':
        
        return render(request, 'loginpage.html' )

    if request.method == 'POST': 
        email_id = request.POST['email']
        password = request.POST['paswd']
        
        
        if Register_form.objects.filter(email=email_id) and Register_form.objects.filter(passewrd=password):

            rie = Register_form.objects.all()
            messages.success( request, "your succssessfully Login in Your Account")
            
            return redirect("dashboard")
        else:
            messages.error( request, "you enterd bad credentials")
            return redirect("userlogin")
    return render(request, 'user dashbord.html', {'fname':rie})

def provider_Login(request):
    
    if request.method == 'GET':
        return render(request, 'providerLogin.html' )

    if request.method == 'POST': 
        email_id = request.POST['Email_id']
        password_p = request.POST['PPassword']
        #user = authenticate(request, email=email_id, password=password_p)
        #if user is not None:
        if Provider_register.objects.filter(email=email_id) and Provider_register.objects.filter(password=password_p ):
            #login(request, user)
            book = Provider_register.objects.get(email=email_id)
            messages.success(request,"You have successfully logged in Your Account")
            return redirect("providerdashboard")
            return render(request, "provider dashaboard.html",{"Profile2":book} ) 

        else:
            messages.error( request, "you enterd bad credentials")
            return redirect("ProviderLogin")
    
def providtexter_addvaickal(request):    
    
    if request.method == 'GET':
        return render(request,"Add vaivkal.html")
    
    if request.method == 'POST':
        valname = request.POST['valname']
        valnumb = request.POST['vaickelnumb']
        val_cost_per_day = request.POST['costperday']
        val_cost_per_hr = request.POST['costperhr']
        valrc = request.FILES['vaiRC']
        valimage = request.FILES['VaImage']
 
        myuser = Addvaickal.objects.create(
            Vai_name  = valname,
            RC = valrc,
            cost =  val_cost_per_day,
            vai_number =valnumb,
            cost_per_hr = val_cost_per_hr,
            image = valimage
        ).save()
        return redirect("textfile")

def providtexter_Login(request):
    rows = Addvaickal.objects.all()
    return render(request, "textfilesdcddd.html", {'names':rows})

def bookvaickel(request):
    
    if request.method == 'GET':
        return render(request,"bookvacel.html") 
    if request.method == 'POST':
        bookname = request.POST['bname']
        bphone = request.POST['bphone']
        license = request.POST["blicence"]
        bookimage = request.POST["BImage"]            #here have one Error fixed

        fromtime = request.POST['fromtime']
        totime = request.POST['totime']


        
        vackeltaker = vaik_taking_user.objects.create(
        name = bookname,
        Phone_valid = bphone,
        licence = license, 
        taker_img = bookimage ,
        time_to_take_days = fromtime,  
        time_in_hr = totime ,
        ).save()
        return redirect("orderbooked")


def ridersuccess(request):
    return render(request, 'order sucssess.html')


'''
def User_Register(request):
    if request.method == 'GET':
        return render(request,"provider register.html") 
    if request.method == 'POST':
        namep = request.POST['name2']
        username = request.POST['username']
        email = request.POST['email2'] 
        passsword  = request.POST['password']

        user = User.objects.create_user(
            first_name = namep,
            username = username,
            email = email,
            password = passsword,
        ).save()
        messages.success(request,'your Account is succssefully Created')
        return redirect("providerdashboard")
    
    '''