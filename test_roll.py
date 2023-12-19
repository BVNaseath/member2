from unittest import TestCase
from roll import Roll
from datetime import date
from club import Club, Member

class TestRoll(TestCase):

    def setUp(self):

        test_members = {"John Smith": "p", "Johnny Doe": "", "Jane Doey": "p"}
        self.roll = Roll(test_members)

    def test_create_roll(self):
        test_members = {"John Smith": "p", "Johnny Doe": "", "Jane Doey": "p"}
        self.assertIsNotNone(self.roll.create_roll(test_members, current_roll = ""))
