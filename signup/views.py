from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponse
#from django.conf.urls import include
from django.template import loader
from django.http import HttpResponseRedirect
from userpage import models


class HomePageView(TemplateView):
    template_name = "signup.html"


def index(request):
        if request.GET.get('sign'):
            models.setUserName(request.GET['uname'])  #Will be test in database in future
            models.setNickName(request.GET['niname'])
            models.setPassword(request.GET['password'])
            return HttpResponseRedirect('/userpage/')
        else:
            return render_to_response('signup.html')

