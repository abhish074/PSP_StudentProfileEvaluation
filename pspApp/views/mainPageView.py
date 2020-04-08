from django.shortcuts import render, redirect



def MainPageView(request):
    return render(request,'mainPage.html')



def AfterLoginView(request):
    return render(request,'afterLogin.html')

