from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            print("valid user")
            return redirect('afterLogin')# html page for redirecting..

        else:
            print("invalid user")
            messages.info(request, 'invalid credentials')
            return redirect('pspApp/login')

    else:
        return render(request, "login.html")
    # return render(request,'login.html')



