from django import forms
from .models import CountFive, CountTen


class CountFiveForm(forms.ModelForm):
    class Meta:
        model = CountFive
        fields = ['number']
        labels = {'number': "Nr. of Priuses seen"}

class CountTenForm(forms.ModelForm):
    class Meta:
        model = CountTen
        fields = ['number']
        labels = {'number': "Nr. of Priuses seen"}