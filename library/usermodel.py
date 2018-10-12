

class User:
    username = ''
    nickname = ''
    password = ''
    dateofbirth = ''
    email = ''
    education = ''
    firstname = ''
    lastname = ''

    def setusername(self, uname):
        global username
        username = uname

    def setnickname(self, niname):
        global nickname
        nickname = niname

    def setfirstname(self, firstn):
        global firstname
        firstname = firstn

    def setlastname(self, lastn):
        global lastname
        lastname = lastn

    def setpassword(self, pword):
        global password
        password = pword

    def setdobirth(self, birth):
        global dateofbirth
        dateofbirth = birth

    def setemail(self, mail):
        global email
        email = mail

    def seteducation(self, edu):
        global education
        education = edu

    def getusername(self):
        return username

    def getnickname(self):
        return nickname

    def getfirstname(self):
        return firstname

    def getlastname(self):
        return lastname

    def getpassword(self):
        return password

    def getdobirth(self):
        return dateofbirth

    def getemail(self):
        return email

    def geteducation(self):
        return education

    def packInfo(self):
        return True

    def setInfo(self):
        return True








