from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.contrib.auth import forms  
from django.contrib.auth.forms import UserCreationForm 
from .models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.

# singup form view

def signup(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['password1']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                 messages.error(request," Username is already taken! ")
                 return render(request,"singup.html")  

            elif User.objects.filter(email=email).exists():
                 messages.error(request," Email is already taken! ")    
                 return render(request,"singup.html")      
 
            else:    
                  user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                  user.save();
                  messages.success(request, "Your account has been sucessfully created you can login now")
                  return render(request, "login.html")
           
        else:
          messages.error(request,"Password not matching")
          return render(request,"singup.html")      
       
    else:
      
        return render(request,"singup.html")      


        

#  login form view
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]


        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "You have successfully logged in !")
            return redirect("/")

        else:
            messages.error(request , "Please enter valid username and password !")    
            return render(request,"login.html")    
    else:
        return render(request,"login.html")      






#  logout yourself

def logout(request):
    auth.logout(request)
    messages.success(request,"You have successfully logged out !")
    return redirect("/")

   
    

# Home Page
def base(request):
    return render(request,"base.html", {"navbar":"/"})
   
    



# Dashboard
@login_required(login_url="/login")
def dashboard(request):
    return render(request,"dashboard.html",{"navbar":"dashboard"})    
    
   
    


# About us Page

@login_required(login_url="/login")
def aboutus(request):
    return render(request,"aboutus.html",{"navbar":"aboutus"})    

   
# Contact us page    
@login_required(login_url="/login")    
def contactus(request):
    if request.method == "POST":
        name1 = request.POST["name1"]
        email1 = request.POST["email1"]
        phone = request.POST["phone"]
        describe = request.POST["describe"]
        if len(name1)<2 or len(email1)<3 or len(phone)<10 or len(describe)<5:
             messages.error(request , "Please fill the form correctly !")  
        else:     
             contact = Contact ( name1=name1, email1=email1, phone=phone, describe=describe)
             contact.save()
             messages.success(request,"Your message has Successfully sent !")
             return redirect("/")


       
   
    return render(request,"contactus.html",{"navbar":"contactus"})   





# not made
def profile(request):
    return render(request,"profile.html")     



# all the dashboards templates
def ipl(request):
    return render(request,"ipl.html")  
    
def sales(request):
    return render(request,"sales.html")  

def crypto(request):
    return render(request,"crypto.html")      
