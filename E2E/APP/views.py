from django.shortcuts import render

from django.http import HttpResponse
from APP import forms
from django.contrib.auth.models import User
from APP import models
# Create your views here.

def index(request):
    registered=False
    items=User.objects.order_by('email')
    if request.method=='POST':

        user_data=forms.user_registry_form(data=request.POST)
        user_pic=forms.profile_stuff_form(data=request.POST)

        if user_data.is_valid() and user_pic.is_valid():

            user=user_data.save()
            user.set_password(user.password)
            user.save()

            user_stuff=user_pic.save(commit=False)
            user_stuff.user=user


            if 'profile_pic' in request.FILES:

                user_stuff.profile_pic=request.FILES['profile_pic']

                user_pic.save(commit=True)
                registered=True
        else:
            print(user_data.errors, user_pic.errors)
    else:

        user_data=forms.user_registry_form()
        user_pic=forms.profile_stuff_form()
    return render(request, 'template/login.html', {'registered': registered, 'user_data': user_data, 'user_pic': user_pic, 'items' : items })


def login(request):

    return render(request, 'template/index.html')

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout




def user_login(request):

    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active():
                login(request, user)

                return HttpResponseRedirect(reverse('index'))

            else:

                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:

            print("someone try to log in and failed")

    else:
        return render(request, 'template/login.html', {})
@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
