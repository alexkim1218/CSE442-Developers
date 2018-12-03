from unittest import TestCase
from homepage.models import Check


class TestCheckUsername(TestCase):
    def test_checkUsernameA(self):
        s = Check
        self.assertTrue(s.checkUsername('fsdasfas'))

    def test_checkUsernameB(self):
        s = Check
        self.assertFalse(s.checkUsername('fs1dasfas'))

