from django import forms
from django.forms import fields, widgets
from django.contrib.auth.models import User
from login_test_app.models import UserInfo 


# default / built in form 
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    

# our custom forms 

class UserInfoForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    class Meta():
        model = UserInfo
        fields = ('address', 'department', 'profile_pic')