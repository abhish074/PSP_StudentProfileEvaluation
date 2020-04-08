from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from pspApp.forms.studentProfileForm import StudentProfileSubmissionForm
from pspApp.models import StudentProfileModel
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'StudentProfileSubmissionForm.html')

def profile(request):
    if request.method == 'POST':
        print("request.post:---", request.POST)
        name = request.user.username
        gre = request.POST['gre']
        workex = request.POST['workex']
        undergrad = request.POST['undergrad']
        quants = request.POST['quants']
        verbal = request.POST['verbal']
        paper = request.POST['paper']
        ielts = request.POST['ielts']
        toefl = request.POST['toefl']

        print("Details:-----", name, workex, quants, verbal)
        print(paper)
        print(type(paper))

        grenumber = int(gre)
        verb = int(verbal)
        quant = int(quants)
        if verb + quant != grenumber:
            return render(request,"QuantsandVerbalSum.html")

        if not StudentProfileModel.objects.filter(name=name).exists():
            StudentProfileModel.objects.create(name=name, gre=gre, workex=workex, undergrad=undergrad, quants=quants,
                                                         verbal=verbal, ielts=ielts, toefl=toefl, paper=paper)

            messages.info(request, "Thank you for submitting your Profile!")
        else:
            StudentProfileModel.objects.filter(name=name).update(name=name, gre=gre, workex=workex, undergrad=undergrad, quants=quants,
                                               verbal=verbal, ielts=ielts, toefl=toefl, paper=paper)
            messages.info(request, "Profile already exists")

        print("sdflsjd")
        return redirect('pspApp/profile_form')

    else:
        print("other")
        return render(request, 'profile_form.html')












