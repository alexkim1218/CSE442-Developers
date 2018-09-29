from HomePage.models import ProfileTb, PhotoTb
from datetime import date as dt


def checkUsrName(usr):
    usrcolumn = list(ProfileTb.objects.values_list('username'))
    usrcolumn = [list(elem) for elem in usrcolumn]
    usrlist = []
    [usrlist.append(elem[0]) for elem in usrcolumn]
    if usr in usrlist:
        return True
    return False


def SubmitSignUp(usr, pwd, usrstory, firstn, lastn, eml, edu, dob):
    if checkUsrName(usr) == False:
        signUpQuery = ProfileTb(username=usr, password=pwd, userstory=usrstory, firstname=firstn, lastname=lastn, email=eml, education=edu, dateofbirth=dob)
        signUpQuery.save()
        return True
    return False

def logIn(usr, pwd):
    if checkUsrName(usr):
        pwdcolumn = list(ProfileTb.objects.values_list('username','password'))
        pwdcolumn = [list(elem) for elem in pwdcolumn]
        pwdlist = []
        [pwdlist.append(elem[0]) for elem in pwdcolumn]
        pwdindex = pwdlist.index(usr)
        if pwd == pwdcolumn[pwdindex][1]:
            return True
    return False

def editProfile(usr, firstn, lastn, eml, dob, edu):
    profile_edit = ProfileTb.objects.get(username=usr)
    profile_edit.firstname = firstn
    profile_edit.lastname = lastn
    profile_edit.email = eml
    profile_edit.dateofbirth = dob
    profile_edit.education = edu
    profile_edit.save()
    return 'Profile edited!'

def submitImage(usr, img, cap):
    d = str(dt.today())
    uploadimage = PhotoTb(username=usr, image=img, date=d, caption=cap)
    uploadimage.save()
    return 'image uploaded!'