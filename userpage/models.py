from django.db import models

# Create your models here.

from django.db import models
usernameV = ""
nicknameV = ""
passwordV = ""


def dbexisted(usern):
    return True

def dbmatch(usern):
    return True

#def dbsetup():  #inplement more in later


def setUserName(usern):
    global usernameV
    usernameV = usern


def setNickName(nname):
    global nicknameV
    nicknameV = nname


def setPassword(pword):
    global passwordV
    passwordV = pword


def getUserName():
    return usernameV


def getNickName():
    return nicknameV


def getPassword():
    return passwordV


