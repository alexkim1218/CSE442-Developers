from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView

from django.http import HttpResponseRedirect
from library.checkinput import Check


class HomePageView(TemplateView):
    template_name = "homepage.html"


def index(request):
        if request.GET.get('log'):
            if Check.checkhomepage(Check, request.GET['uname'], request.GET['password']):
                return HttpResponseRedirect('/userpage/')
            else:
                error = Check.geterror(Check)
                return render(request, 'homepage.html', {'errormsg': [error]})
        elif request.GET.get('sig'):
            return HttpResponseRedirect('/signup/')
        else:
            return render_to_response('homepage.html')
