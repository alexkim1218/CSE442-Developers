from unittest import TestCase
from mysite.homepage.models import Check


class TestCheck(TestCase):
    def test_checkPassword(self):
        s = Check
        self.assertFalse(s.checkPassword('%#@&12'))

    def test_checkPasswordB(self):
        s = Check
        self.assertFalse(s.checkPassword('%#@&12%&*'))

    def test_checkPasswordC(self):
        s = Check
        self.assertTrue(s.checkPassword('Jopdh1ui4'))

    def test_checkPasswordD(self):
        s = Check
        self.assertFalse(s.checkPassword('Jopd#$h1ui4'))

    def test_checkPasswordE(self):
        s = Check
        self.assertFalse(s.checkPassword('gdshssddb'))

    def test_checkPasswordF(self):
        s = Check
        self.assertFalse(s.checkPassword('ASDRTYIOPU'))

    def test_checkPasswordF(self):
        s = Check
        self.assertFalse(s.checkPassword('1234567856'))

    def test_checkPasswordF(self):
        s = Check
        self.assertFalse(s.checkPassword(''))


