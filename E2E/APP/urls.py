from django.contrib import admin
from django.urls import path, include
from APP import views

app_name='template'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('user_login/', views.user_login, name='user_login')




]
