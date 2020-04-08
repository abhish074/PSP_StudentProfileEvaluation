from django import forms
from pspApp.models import StudentProfileModel
from django.forms import ModelForm
from django import forms



class StudentProfileSubmissionForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    gre = forms.IntegerField(required=False)
    paper = forms.CharField(max_length=100)
    workex = forms.IntegerField()
    undergrad = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input100 '
                                    , 'min':'5.0', 'max':'10.0',
                                       'required': True}))
    quants = forms.IntegerField()
    verbal = forms.IntegerField()
    ielts = forms.FloatField()
    toefl = forms.IntegerField()
    class Meta:

        model = StudentProfileModel
        fields = '__all__'

    def clean_undergrad(self, *args, **kwargs):
        # cleaned_data = super().clean()
        # super(StudentProfileSubmissionForm, self).clean
        undergrad = self.cleaned_data.get('undergrad')
        if undergrad < 10:
            return undergrad
        else:
            raise forms.ValidationError("Ungrad score should be less than 10")




