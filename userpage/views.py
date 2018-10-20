from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponse
#from django.conf.urls import include
from django.template import loader
from django.http import HttpResponseRedirect
from signup import views
from userpage import models


class UserPageView(TemplateView):
    template_name = "userpage.html"


def index(request):
        if request.GET.get('sigt'):
            return HttpResponseRedirect('/homepage/')
        elif request.GET.get('edit'):
            return HttpResponseRedirect('/userprofile/')
        else:
            return render(request, 'userpage.html', {'nickname': 'Admin'})


