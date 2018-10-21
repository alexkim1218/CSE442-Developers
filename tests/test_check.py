from unittest import TestCase
from library.checkinput import Check

class TestCheck(TestCase):
    def test_checkusernameA(self):
        s = Check
        self.assertTrue(s.checkusername('fasdfs'))

    def test_checkusernameB(self):
        s = Check
        self.assertTrue(s.checkusername('fafsdsdfs'))


    def test_checknicknameA(self):
        s = Check
        self.assertTrue(s.checknickname('fdsad'))

    def test_checknicknameB(self):
        s = Check
        self.assertFalse(s.checknickname('fdsadfdsfsd'))

    def test_checknicknameC(self):
        s = Check
        self.assertFalse(s.checknickname('fdsad32'))

    def test_checknicknameD(self):
        s = Check
        self.assertFalse(s.checknickname('fdsad!/.'))

    def test_checknicknameE(self):
        s = Check
        self.assertTrue(s.checknickname('William'))
