from unittest import TestCase
from mysite.homepage.models import Check


class TestCheckUsername(TestCase):
    def test_checkUsernameA(self):
        s = Check
        self.assertTrue(s.checkUsername('fsdasfas'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername('fs1dasfas'))

    def test_checkUsernameA(self):
        s = Check
        self.assertTrue(s.checkUsername('jaswinderkau'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername('123456789123'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername('jaswinderka%'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername('#fs1dasfas'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername('!@#$%&*'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername(''))

