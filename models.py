#from django.db import models

# Create your models here.


from userpage import models

class Check():

    def checkUsername(uname):  # checking valid username

        while len(uname) <= 12:
            for loop in uname:
                if loop == '1':
                    return False
                elif loop == '2':
                    return False
                elif loop == '3':
                    return False
                elif loop == '4':
                    return False
                elif loop == '5':
                    return False
                elif loop == '6':
                    return False
                elif loop == '7':
                    return False
                elif loop == '8':
                    return False
                elif loop == '9':
                    return False
                elif loop == '0':
                    return False
                elif loop == '!':
                    return False
                elif loop == '@':
                    return False
                elif loop == '#':
                    return False
                elif loop == '%':
                    return False
                elif loop == '$':
                    return False
                elif loop == '&':
                    return False
                elif loop == '*':
                    return False
                elif loop == '.':
                    return False
                elif loop == ',':
                    return False


            else:
                if len(uname) == 0:
                    return False
                else:
                    return True

    def checkPassword(pword):

       while (len(pword) > 8) and (len(pword) <= 16):
            for loop_i in pword:
                if loop_i == '*':
                    return False
                elif loop_i == '#':
                    return False
                elif loop_i == '!':
                    return False
                elif loop_i == '&':
                    return False
                elif loop_i == '%':
                    return False
                elif loop_i == '$':
                    return False
                elif loop_i == '@':
                    return False
                elif loop_i == ',':
                    return False
                elif loop_i == '.':
                    return False
                elif not any(loop_i.isupper() for loop_i in pword):
                    return False
                elif not any(loop_i.islower() for loop_i in pword):
                    return False
                elif not any(loop_i.isdigit() for loop_i in pword):
                    return False
            else:
                return True

    def checkIn(uname,pword):
        models.setUserName(uname)
        models.setPassword(pword)
        return 'User Has Check In.'


#class UserTb(models.Model):
#    user = models.CharField(max_length=20, blank=True, null=True)
#    password = models.CharField(max_length=20, blank=True, null=True)

#    class Meta:
#        managed = False
#        db_table = 'user_tb'

#    def user_exist(self, usr):
#        try:
#            usr = UserTb.objects.filter('user')
#        except:
#            return UserTb.DoesNotExist

#    def login_verify(self, usr, pwd):
#            user_valid = UserTb.objects.filter()
#            pass_valid = UserTb.objects.get()
#            if user_valid and pass_valid:
#                return True
#            else:
#                return False


#class login():
#    def signup(self):
#        b = UserTb(user='username', password='pass')
#        b.save()


#class usrpass():
#    def __init__(self):
#        self.user = 'username'

#    def __init__(self):
#        self.password = 'pass'








