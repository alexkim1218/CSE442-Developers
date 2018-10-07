#from django.db import models

# Create your models here.
from userpage import models


class Check:
    def checkUsername(uname):    #Checking Valid Username
        if '1' not in uname:
            return True
        else:
            return False

    def checkPassword(pword):    #Checking Vaild Password
        return False

    def checkIn(uname, pword):   #Check In User
        models.setUserName(uname)
        models.setPassword(pword)
        return 'User Has Check In.'