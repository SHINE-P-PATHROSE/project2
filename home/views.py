from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib import messages
from django.http import HttpResponse
def home (request):
    return render(request, 'home.html')

def form (request):
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email= request.POST['email']
            pass1= request.POST['pass1']
            pass2 = request.POST['pass2']

            # Check if the username or email already exists
            if User.objects.filter(username=username).exists():
                print("User not created: Username already exists")
                return HttpResponse("Username already exists.")
            elif User.objects.filter(email=email).exists():
                print("User not created: Email already exists")
                return HttpResponse("Email already exists.")
            else:
                # Create and save the user if the conditions are met
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname)
                user.save()
                print("User created")
                return redirect('/')
        return render(request,'form.html')



def login (request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"user not find")
            return redirect("login")
    else:
        return render(request,"login.html")