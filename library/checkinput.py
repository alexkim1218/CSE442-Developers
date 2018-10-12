import string


class Check:

    error = ''

    def checkusername(uname):
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

    def checknickname(niname):
        if len(niname) >= 8:
            return False
        for c in niname:
            if c.isdigit():
                return False
            if c in set(string.punctuation):
                return False

        return True

    def checkpassword(pword):
        while (len(pword) >= 8) and (len(pword) <= 16):
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

    def checkdateofbirth(birth):
        return True

    def checkhomepage(self, uname, pword):
        global error
        if (self.checkusername(uname) and self.checkpassword(pword)) is False:
            error = 'You entered invalid Username or Password!!!!!'
            return False
        elif self.checkdatabasehomepage(uname, pword) is False:
            error = 'You need to sign Up!!!!!'
            return False
        else:
            return True

    def checkdatabasehomepage(uname, pword):
        return True

    def geterror(self):
        return error

    def checksignuppage(self,uname,niname,pword,birth):
        return self.checkusername(uname) and self.checknickname(niname) and self.checkpassword(pword) and \
               self.checkdateofbirth(birth)

