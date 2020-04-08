from django import forms
from django.forms import ModelForm

from django.contrib.auth import (

    authenticate,
    get_user_model, #used when you use custom user for login purpose...

)

#the following helps to get the user model which we custom defined..
#that is it helps us to get the user at the time of the creating the user from the backend...

User = get_user_model()


class studentRegisterForm(forms.ModelForm):

    studentEmail = forms.EmailField(label='Enter a valid Email Address')
    confirmStudentEmail = forms.EmailField(label='Confirm Email Address')
    studentPassword = forms.CharField(widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = [
            'username',
            'studentEmail',
            'confirmStudentEmail',
            'studentPassword'
        ]

    def clean_email(self):
        studentEmail = self.cleaned_data.get('studentEmail')
        confirmStudentEmail = self.cleaned_data.get('confirmStudentEmail')
        #studentPassword = self.cleaned_data.get('studentPassword')

        if studentEmail != confirmStudentEmail:
            raise forms.ValidationError('Emails does not match')

        email_qs =  User.objects.filter(studentEmail = studentEmail)

        if email_qs.exists():
            raise forms.ValidationError('This email already exists')

        return studentEmail









