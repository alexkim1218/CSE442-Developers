from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponse
#from django.conf.urls import include
from django.template import loader

from django.http import HttpResponseRedirect
from homepage.models import Check

class HomePageView(TemplateView):
    template_name = "homepage.html"


def index(request):
        if request.GET.get('log'):
            if Check.checkUsername(request.GET['uname']) and Check.checkPassword(request.GET['password']):
                print(Check.checkIn())
                return HttpResponseRedirect('/userpage/')
            else:
                return render(request, 'homepage.html', {'errormsg': ['You have invaild Username or Password!!!!']})
        elif request.GET.get('sig'):
            return HttpResponseRedirect('/signup/')
        else:
            return render_to_response('homepage.html')
