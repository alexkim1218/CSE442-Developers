#from django.db import models

# Create your models here.
from userpage import models


class Check:

    def checkIn(uname, pword):   #Check In User
        models.setUserName(uname)
        models.setPassword(pword)
        return 'User Has Check In.'

