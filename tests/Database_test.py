from django.test import TestCase, TransactionTestCase
from home.checkinput import Check
from home import db_functions
from home.models import ProfileTb, PhotoTb, ChatTb


class TestCheck(TestCase):
    def test_checkusernameA(self):
        s = Check
        self.assertTrue(s.checkusername('fasdfs'))

    def test_checkusernameB(self):
        s = Check
        self.assertTrue(s.checkusername('fafsdsdfs'))

    def test_checkusernameC(self):
        s = Check
        self.assertFalse(s.checkusername('fsafd2'))

    def test_checknicknameA(self):
        s = Check
        self.assertTrue(s.checknickname('fdsad'))

    def test_checknicknameB(self):
        s = Check
        self.assertTrue(s.checknickname('fdsadfdsfsd'))

    def test_checknicknameC(self):
        s = Check
        self.assertFalse(s.checknickname('fdsad32'))

    def test_checknicknameD(self):
        s = Check
        self.assertFalse(s.checknickname('fdsad!/.'))

    def test_checknicknameE(self):
        s = Check
        self.assertTrue(s.checknickname('William'))

    def test_checkdateofbirthA(self):
        s = Check
        self.assertTrue(s.checkdateofbirth(Check, '08201996'))

    def test_checkdateofbirthB(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '01361996'))

    def test_checkdateofbirthC(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '13201996'))

    def test_checkdateofbirthD(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '03321996'))

    def test_checkdateofbirthE(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '02281996'))

    def test_checkdateofbirthF(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '02291997'))

    def test_checkdateofbirthG(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '06202020'))

    def test_checkpasswordA(self):
        s = Check
        self.assertFalse(s.checkpassword('06202020'))

    def test_checkpasswordA(self):
        s = Check
        self.assertFalse(s.checkpassword('06202020'))

    def test_checkpasswordB(self):
        s = Check
        self.assertFalse(s.checkpassword('A06202020'))

    def test_checkpasswordC(self):
        s = Check
        self.assertFalse(s.checkpassword('a06202020'))

    def test_checkpasswordD(self):
        s = Check
        self.assertFalse(s.checkpassword('A062020'))

    def test_checkpasswordE(self):
        s = Check
        self.assertTrue(s.checkpassword('Aa06202020'))

    def test_checkemailA(self):
        s = Check
        self.assertFalse(s.checkemail(Check, 'fsfdsfds'))

    def test_checkemailB(self):
        s = Check
        self.assertFalse(s.checkemail(Check, 'fsfdsfds.com'))

    def test_checkemailC(self):
        s = Check
        self.assertFalse(s.checkemail(Check, 'fsfdsfds@.com'))

    def test_checkemailD(self):
        s = Check
        self.assertFalse(s.checkemail(Check, 'fsfdsfds@gfgfd'))

    def test_checkemailE(self):
        s = Check
        self.assertFalse(s.checkemail(Check, 'fsfdsfds.comfds@fds'))

    def test_checkemailF(self):
        s = Check
        self.assertFalse(s.checkemail(Check, 'fsf.edudsfds@buffalo'))

    def test_checkemailG(self):
        s = Check
        self.assertTrue(s.checkemail(Check, 'weibinhu@buffalo.edu'))

    def test_checkgenderA(self):
        s = Check
        self.assertTrue(s.checkgender(Check, 'M'))

    def test_checkgenderB(self):
        s = Check
        self.assertTrue(s.checkgender(Check, 'F'))

    def test_checkgenderC(self):
        s = Check
        self.assertTrue(s.checkgender(Check, 'm'))

    def test_checkgenderD(self):
        s = Check
        self.assertTrue(s.checkgender(Check, 'f'))

    def test_checkgenderE(self):
        s = Check
        self.assertFalse(s.checkgender(Check, 'M13'))

    def test_checkgenderF(self):
        s = Check
        self.assertFalse(s.checkgender(Check, 'MMMMMM'))

    def test_checkgenderF(self):
        s = Check
        self.assertFalse(s.checkgender(Check, '+'))


class DataBaseTestCheck(TransactionTestCase):
    def setUp(self):
        ProfileTb.objects.create(username='testusr', password='testpwd', userstory='',
                                 firstname='testfirstname', lastname='testlastname', email='test@test.com',
                                 education='UB', dateofbirth='11201995', gender='M')

    def test_login(self):
        dic = {}
        self.assertEqual(type(db_functions.logIn('testusr', 'testpwd')), type(dic))

    def test_homepageview(self):
        dic = {}
        dictP = db_functions.homepgView('testusr')
        self.assertEqual(type(dictP), type(dic))
        self.assertTrue(dictP['firstname'] == 'testfirstname')
        self.assertTrue(dictP['lastname'] == 'testlastname')
        self.assertTrue(dictP['email'] == 'test@test.com')
        self.assertTrue(dictP['dateofbirth'] == '11201995')
        self.assertTrue(dictP['gender'] == 'M')

    def test_signup(self):
        self.assertEqual(db_functions.SubmitSignUp('testusr2', 'testpwd', 'my name is test', 'testfirstname', 'testlastname',
                                              'test@test.com', 'testUB', '11201995', 'M'), True)

    def test_editprofile(self):
        self.assertEqual(db_functions.editProfile('testusr', 'testfname', 'testlastname',
                                                  'test@test.com', '11201995', ''), 'Profile edited!')

    def test_adduserstory(self):
        db_functions.adduserstory('testusr', 'Hello')
        self.assertEqual(db_functions.getuserstory('testusr')[1], 'Hello')

    def test_addfriend(self):
        self.assertFalse(db_functions.addFriend('testusr', 'testusr'))
        self.assertEqual(db_functions.getFriend('testusr'), '')

