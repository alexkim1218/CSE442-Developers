from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from library.usermodel import User
from friends.models import ProfileTb, PhotoTb
from library import databasecheck



class UserPageView(TemplateView):
    template_name = "displayfriends.html"


def index(request):
        if request.GET.get('addfriend'):
            if databasecheck.addFriend(User.getusername(User), request.GET['search']):
                print('I am here')
                User.setfriend_list(User, databasecheck.friendsList(User.getusername(User)))
                return render(request, 'displayfriends.html', {'friend_list': User.getfriend_list(User)})
            else:
                return HttpResponseRedirect('/friend_list/')
        elif request.GET.get('button'):
            print(request.GET['button'])
            dictF = databasecheck.homepgView(request.GET['button'])

            return render(request,'detail-modal.html', {'first_name': dictF['firstname'],
                                                        'last_name' :  dictF['lastname'],
                                                        'friend_email':  dictF['email'],
                                                        'friend_dob': dictF['dateofbirth'],
                                                        'friend_edu': dictF['education'],})

        elif request.GET.get('bth'):
            return HttpResponseRedirect('/userpage/')
        else:
            return render(request, 'displayfriends.html', {'friend_list': User.getfriend_list(User)})
