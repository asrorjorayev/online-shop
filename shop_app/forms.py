from typing import Any
from django import forms
from .models import User


class LoginForm(forms.Form):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean_username(self):
        username=self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('username mavjud emas')


class RegisterForm(forms.Form):
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        password=self.cleaned_data.get('password',None)
        confirm_password=self.cleaned_data.get('confirm_password',None)
        if password:
            if confirm_password != password:
                raise forms.ValidationError("Parol ni bir xil kiriting ")
        return self.cleaned_data
    
class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(required=True,disabled=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','password')
