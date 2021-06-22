from django import forms
from APP.models import user_registery_model
from django.forms import ModelForm
from django.contrib.auth.forms import User

class user_registry_form(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():

        fields=('username', 'password', 'email')
        model=User

class profile_stuff_form(forms.ModelForm):
    class Meta():
        model=user_registery_model
        fields=('profile_pic', 'profile_site')
