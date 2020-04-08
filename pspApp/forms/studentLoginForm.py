from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

class studentLoginForm(forms.Form):
    studentUserName = forms.CharField()
    studentPassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kargs):
        studentUserName = self.cleaned_data.get("studentUserName")
        studentPassword = self.cleaned_data.get("studentPassword")


        if studentUserName and studentPassword:
            user = authenticate(username = studentUserName , password = studentPassword )

            if not user:
                raise forms.ValidationError('User does not exist')

            if not user.check_password(studentPassword):
                raise forms.ValidationError('Incorrect password')

        return super(studentLoginForm,self).clean(*args,**kargs)
