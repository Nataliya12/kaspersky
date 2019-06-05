# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    e_mail = forms.CharField(label=None, widget=forms.TextInput(attrs={  
            'placeholder': u'', 'class':"form-control"}))
    password = forms.CharField(label='Пароль',  widget=forms.PasswordInput(attrs={  
            'placeholder': u'', 'class':"form-control"}))

    def clean_e_mail(self):
        e_mail = self.cleaned_data.get('e_mail')
        if e_mail:
            if not User.objects.filter(username=e_mail):
                raise forms.ValidationError('Пользователь в системе не зарегистрирован')
        return e_mail


def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            a =  User.objects.filter(username=password)
            if a:
                raise forms.ValidationError('Пароль неверен')
        return password


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя',   widget=forms.TextInput(attrs={  
            'class':"form-control"}))
    family = forms.CharField(label='Фамилия',  widget=forms.TextInput(attrs={  
            'class':"form-control"}))
    e_mail = forms.EmailField(label='Ваш e-mail', widget=forms.TextInput(attrs={  
            'class':"form-control"}))
    password = forms.CharField(label='Пароль ',  widget=forms.PasswordInput(attrs={  
            'class':"form-control"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={  
            'class':"form-control"}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError('Пароли не совпадают')
        return password2
    
    def clean_e_mail(self):
        e_mail = self.cleaned_data.get('e_mail')
        if e_mail:
            a = User.objects.filter(username=e_mail)
            if a:
                raise forms.ValidationError('Пользователь существует')
        return e_mail