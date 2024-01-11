from django import forms

from app.models import *

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields="__all__"
    botCacher=forms.CharField(max_length=50,required=False,widget=forms.HiddenInput)


    def clean_botCacher(self):
        b=self.cleaned_data['botCacher']
        if len(b)>0:
            raise forms.ValidationError('Invalid Data....')