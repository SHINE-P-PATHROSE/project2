from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
def home (request):
    return render(request, 'home.html')

def form(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            # Check if the username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect("form")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect("form")
            else:
                # Create and save the user if the conditions are met
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname)
                user.save()
                print("User created")
                return redirect('/')
        else:
            print('Password not matched')
            messages.info(request, 'Password not matched')
            return redirect('form')
    else:
        return render(request, 'form.html')


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



def logout(request):
    auth.logout(request)
    return redirect('/')