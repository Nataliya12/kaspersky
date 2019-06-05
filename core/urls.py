from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', index),
    path('login/', login),
    path('registration/', registration),
    path('registration_success/', registration_success),
    path('available/', available, name='available'),
    path('logout/', LogoutView.as_view(template_name='logout.html')),
    path('tests/', tests),
    path('test/<int:id>/', test_id),
    path('bosch/', bosch),
    path('teaching/', teaching, name='teaching'),
    path('teaching/antivirus/', antivirus, name='antivirus'),
    path('teaching/kpm/', kpm, name='kpm'),
    path('teaching/ksk/', ksk, name='ksk'),
    path('teaching/myk/', myk, name='myk'),
    path('teaching/ksec/', ksec, name='ksec'),
    path('tests1/', tests1),
    path('tests2/', tests2),
    path('tests3/', tests3),
    path('tests4/', tests4),
    path('tests5/', tests5),
]
