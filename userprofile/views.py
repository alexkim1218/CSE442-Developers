from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from library.usermodel import User


class UserPageView(TemplateView):
    template_name = "userprofile.html"


def index(request):
        if request.GET.get('save'):
            User.setInfo(User)
        elif request.GET.get('cancel'):
            return HttpResponseRedirect('/userpage/')
        else:
            return render_to_response('userprofile.html')

