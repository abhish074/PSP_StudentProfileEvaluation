from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from pspApp.views import profileFormView, studentLoginView, studentRegisterView, mainPageView, resultView





urlpatterns = [
    #127.0.0.1:8000/
    url(r'^$', profileFormView.home, name='home'),

    # url(r'studentLogin', studentLoginView.studentLoginView, name='studentLoginView'),
    # url(r'studentRegister', studentRegisterView.studentRegisterView, name='studentRegisterView'),

    ##Below URLs for the student login and register page...
    ## use view name in anchor tags inside htmls, for hyperlinking..
    #for example name='studentRegister' is used in mainPage for hyperlinking login page
    url(r'register', studentRegisterView.RegisterView, name='studentRegister'),## Student registration Page
    url(r'login', studentLoginView.LoginView, name='studentLogin'),## Student Login Page

    ## Bokeh plot view...
    url(r'header', resultView.viewResult, name='header'),

    url(r'afterLogin/prediction', resultView.PredictionView, name='prediction'),

    # url(r'universities_result', resultView.bokehPlotView, name='universities_result'),

    ## Following is the main page view.
    # The first is the landing page
    url(r'mainPage', mainPageView.MainPageView, name='mainPage'),  ## Student Login Page

    #This page will appear once user logs in!
    url(r'afterLogin', mainPageView.AfterLoginView, name='afterLogin'),  ## Student Login Page

    ## Bokeh plot view...

    # this is the page where a user is asked to create profile..
    # generates a form for creating a profile..
    # url(r'profile', profileFormView.profile, name='index'),

    url(r'profile', profileFormView.profile, name='profile_form'),

    #Admin dashboard.
    url(r'^admin/', admin.site.urls),
]

