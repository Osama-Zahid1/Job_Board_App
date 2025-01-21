from django import forms
from .models import Seekermodel,Recruitermodel,Application
from django.core.exceptions import ValidationError

class Seekeregform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Seekermodel
        fields=['username','email','degree','experience','address','skills','pic','resume']


class seekerupform(forms.ModelForm):

    class Meta:
        model = Seekermodel
        fields = ['username', 'email', 'degree', 'experience', 'address', 'skills', 'pic', 'resume']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Seekermodel.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email is already in use.")
        return email

class recruiterupform(forms.ModelForm):
    

    class Meta:
        model = Recruitermodel
        fields = ['username', 'email', 'businessname', 'businesstype', 'address']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Recruitermodel.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email is already in use.")
        return email





class Recruiterregform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Recruitermodel
        fields = ['username', 'email', 'businessname', 'businesstype', 'address']  # Include 'businessname' and 'businesstype' fields

        
class RegistrationTypeForm(forms.Form):
    USERTYPE_CHOICES = [ # as we dont have constant mentioned here we can just write the value one that we will store and value two that is human readable
        ('seek', 'Seeker'),
        ('recruit', 'Recruiter'),
    ]
    ustype= forms.ChoiceField(label='User Type', choices=USERTYPE_CHOICES, widget=forms.RadioSelect)
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']