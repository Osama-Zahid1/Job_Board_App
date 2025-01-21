from seekerapp.models import Jobmodel
from django import forms

class Jobform(forms.ModelForm):
    class Meta:
        model=Jobmodel
        fields=[ 'jobtitle','jobdesp','skillsreq','businessadd','salary']
        

    
