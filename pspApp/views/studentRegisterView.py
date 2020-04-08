from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



def RegisterView(request):
    if request.method == 'POST':
        # firstName = request.POST['firstName']
        # lastName = request.POST['lastName']
        print("sample")
        username = request.POST['username']
        email = request.POST['email']
        confirmEmail = request.POST['confirmemail']

        password = request.POST['password']
        if email == confirmEmail:
            if User.objects.filter(username=username).exists():
                print("Username taken")
                messages.info(request, 'Username Taken')
                return redirect('pspApp/register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')

                return redirect('pspApp/register')

            else:
                user = User.objects.create_user(username=username,  email=email, password=password,
                                               )
                user.save()
                print("User created")
                return redirect('pspApp/login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('RegisterView')## view name in the redirect
    else:
        print("other")
        return render(request, 'register.html')  ## html name in the render

    # return render(request,'register.html')


# def studentRegisterView(request):
#
#     #we get the value of the next..
#     #this value will help us to redirect the user to the page we want..
#     resgister_form = studentRegisterForm()
#     next = request.GET.get('next')
#     if request.method == 'POST':
#         form = studentRegisterForm(request.POST or None)
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data.get('studentUserName')
#             password = form.cleaned_data.get('studentPassword')
#             user.set_password(password)
#             user.save()
#             new_user = authenticate(username=username, password=password)
#             login(request, user)
#             if next:
#                 print("inside next")
#                 return redirect(next)
#             return HttpResponse("thankyou for registering")
#
#     # context = {
#     #     'form':form
#     #
#     # }
#     print("not registered")
#     return render(request, 'studentRegister.html', {'form': resgister_form})
#

