"""studentforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/',Homepage.as_view(),name="backend"),
    path('signin/',Signin.as_view(),name="Signin"),
    path('signup/',Signup.as_view(),name="Signup"),
    path('issignedin/',IsSignedIn.as_view(),name="IsSignedIn"),
    path('question/',AskQuestion.as_view(),name="question"),
    path('loadQuestions/',LoadQuestions.as_view(),name="loadQuestions"),
    path('loadAllAnswers/',LoadAllAnswers.as_view(),name="loadAllQuestions"),
    path('signout/',Signout.as_view(),name="signout"),
    path('getuser/',GetUserById.as_view(),name="getUserById"),
    path('postAnswer/',PostAnswer.as_view(),name="postAnswer"),
    path('check/',Check.as_view(),name="check"),
    path('search/',Search.as_view(),name="search"),
]
