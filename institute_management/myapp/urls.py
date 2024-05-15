"""
URL configuration for institute_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.student, name='student'),
    path('teacher', views.teacher, name='teacher'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('viewstudent', views.viewstudent, name='viewstudent'),
    path('addteacher', views.addteacher, name='addteacher'),
    path('viewteacher', views.viewteacher, name='viewteacher'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('sprofile', views.sprofile, name='sprofile'),
    path('tprofile', views.tprofile, name='tprofile'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('fpassword_email', views.fpassword_email, name='fpassword_email'),
    path('password', views.password, name='password'),
    path('email_newpassword', views.email_newpassword, name='email_newpassword'),
    path('sdetail', views.sdetail, name='sdetail'),
    path('tdetail', views.tdetail, name='tdetail'),
]
