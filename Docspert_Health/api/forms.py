from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_select2.forms import Select2Widget


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class CsvFileForm(forms.ModelForm):
    class Meta:
        model = CsvFiles
        fields = ['file']
        

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['accounts_from','accounts_to','amount']
        widgets = {
            'accounts_from': Select2Widget,
            'accounts_to': Select2Widget,
        }



class SearchForm(forms.Form):
    account = forms.CharField()