from django.test import TestCase, TransactionTestCase
from HomePage import main_db
from HomePage.models import ProfileTb

class DatabaseTestCase(TransactionTestCase):
    def setUp(self):
        ProfileTb.objects.create(username='testusr', password='testpwd', userstory='my name is test', firstname='testfirstname', lastname='testlastname', email='test@test.com', education='UB', dateofbirth='11201995')
        # main_db.SubmitSignUp('testusr', 'testpwd','my name is test','testfirstname', 'testlastname','test@test.com','testUB','11201995')
    def test_login(self):
        dic = {}
        self.assertEqual(type(main_db.logIn('testusr', 'testpwd')), type(dic))
    def test_homepageview(self):
        dic = {}
        self.assertEqual(type(main_db.homepgView('testusr')), type(dic))
    def test_signup(self):
        self.assertEqual(main_db.SubmitSignUp('testusr2', 'testpwd','my name is test','testfirstname', 'testlastname','test@test.com','testUB','11201995'), True)