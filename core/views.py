# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.forms import *
from core.models import *
from django.http import HttpResponseRedirect
from django.conf import settings


def index(request):
    return render(request, 'homepage.html')

def login(request):
    form1 = AuthForm(request.POST)
    if request.method == "POST":
        form = AuthForm(request.POST)
        if "first_form" in request.POST:
            if form.is_valid(): 
                username = form.cleaned_data.get('e_mail', None)
                password = form.cleaned_data.get('password', None)
                
                
                user = authenticate(request, username=username, password=password)   
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect("/available/")
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form':form,})

def registration(request):
    form2 = RegistrationForm(request.POST)
    if "second_form" in request.POST:
            if form2.is_valid(): 
                username = form2.cleaned_data.get('e_mail', None)
                password = form2.cleaned_data.get('password', None)
                password2 = form2.cleaned_data.get('password2', None)
                name = form2.cleaned_data.get('name', None)
                family = form2.cleaned_data.get('family', None)
                registr = User.objects.create_user(username=username, password=password)
                registr.save()
                UserProfile.objects.create(user = registr, nameuser = name, family = family)
                user = authenticate(request, username=username, password=password)   
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect('/registration_success/')
           
    else:
        form2 = RegistrationForm()
    return render(request, 'registration.html', {'form2':form2,})

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect("/logout/")


def registration_success(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    return render(request, 'registration_success.html')


def bosch(request):
    template = 'bosch.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})

def available(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'available.html'
    return render(request,
                  template
                  )

def teaching(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'teaching.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})


def antivirus(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'antivirus.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})

def kpm(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'kpm.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})

def ksk(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'ksk.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})

def myk(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'myk.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})

def ksec(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    template = 'ksec.html'
    TextAll = Text.objects.all()
    return render(request,
                  template,
                  {"TextAll": TextAll})
     
def tests(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    objects = ModelTestirovanie.objects.all()
    return render(request, 'tests.html', {'objects':objects})


def tests1(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    objects = ModelTestirovanie.objects.all()
    return render(request, 'tests-1.html', {'objects':objects})

def tests2(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    objects = ModelTestirovanie.objects.all()
    return render(request, 'tests-2.html', {'objects':objects})

def tests3(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    objects = ModelTestirovanie.objects.all()
    return render(request, 'tests-3.html', {'objects':objects})
    
def tests4(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    objects = ModelTestirovanie.objects.all()
    return render(request, 'tests-4.html', {'objects':objects})

def tests5(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    objects = ModelTestirovanie.objects.all()
    return render(request, 'tests-5.html', {'objects':objects})



def test_id(request,id):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')
    testget = ModelTestirovanie.objects.get(id=id)
    
    if request.method == "POST":
        if "oneanswer" in request.POST:
            id_question = request.POST.get('idvopros')
            id_answer = request.POST.get('optionsradios')
            answer_for_bd = ModelTestAnswer.objects.get(id=id_answer)
            answer_user = ModelTestAnswerUser.objects.get(id=id_question)
            if answer_for_bd.status == True:
                res = 1
            else:
                res = 0
            
            answer_user.answer = answer_for_bd.otvet
            
            answer_user.result = res
            answer_user.status_answer=True
            answer_user.save()
            return redirect('/test/%s' % id)
    
    
    if not ModelTestirovanieUser.objects.filter(userid=request.user, modeltest=testget):
        modeltestuser = ModelTestirovanieUser.objects.create(userid=request.user, modeltest=testget)
        testquestions = ModelTestQuestions.objects.filter(modeltest=testget)
        for i in testquestions:
            if not ModelTestAnswerUser.objects.filter(questions=i, modeltestirovanieuser=modeltestuser):
                ModelTestAnswerUser.objects.create(questions=i, modeltestirovanieuser=modeltestuser)
    else:
        modeltestuser = ModelTestirovanieUser.objects.get(userid=request.user, modeltest=testget)
        if modeltestuser.status == False:
            testquestions = ModelTestQuestions.objects.filter(modeltest=testget)
            for i in testquestions:
                if not ModelTestAnswerUser.objects.filter(questions=i, modeltestirovanieuser=modeltestuser):
                    
                    ModelTestAnswerUser.objects.create(questions=i, modeltestirovanieuser=modeltestuser)
    
    
    questions_for_user_false = ModelTestAnswerUser.objects.filter(modeltestirovanieuser=modeltestuser, status_answer=False).order_by('?')
    questions_for_user_all = ModelTestAnswerUser.objects.filter(modeltestirovanieuser=modeltestuser)
    
    
    sum = 0 
    questions_for_user_result = ModelTestAnswerUser.objects.filter(modeltestirovanieuser=modeltestuser, status_answer=True)
    for i in questions_for_user_result:
        sum = sum+i.result
    
        
    return render(request, 'testget.html', {'testget':testget,'questions_for_user_false':questions_for_user_false,'sum':sum,'questions_for_user_all':questions_for_user_all})
    
    
    
    
    