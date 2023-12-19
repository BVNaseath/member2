from unittest import TestCase
from club import Member,  Club
from roll import Roll
from datetime import date


class TestClub(TestCase):

    def setUp(self):
        test_members = [['John Smith', '123 Main St', '(555) 555-1212'],
                   ['Jane Doe', '456 Oak St', '(555) 555-2323'],
                   ['Bob Johnson', '789 Maple Ave', '(555) 555-3434']]
        members = [Member(item[0], item[1], item[2]) for item in test_members]
        self.club = Club('TSA', members)

    def test_add_member(self):
        self.assertEqual(3, len(self.club.members))
        self.club.add_member('Frank Lee', '456 Shady Lane', '555-1212')
        self.assertEqual(4, len(self.club.members))
        self.assertIsNotNone(self.club.find_member('Frank Lee'))

    def test_find_member(self):
        self.assertIsNotNone(self.club.find_member('John Smith'))

    def test_find_member_none(self):
        self.assertIsNone(self.club.find_member("John smieth"))

    def test_remove_member(self):
        self.club.remove_member("John Smith")
        self.assertIsNone(self.club.find_member("John Smith"))

    def test_new_address(self):
        self.club.new_address('John Smith', '123 center St')
        member = self.club.find_member("John Smith")
        self.assertEqual(member.address, "123 center St")
    def test_new_phone_number(self):
        self.club.new_phone_number('John Smith', '(555)-555-5555')
        member = self.club.find_member("John Smith")
        self.assertEqual(member.phone_number, "(555)-555-5555")
    def test_change_name(self):
        self.club.change_name('John Smith', 'Johnny Smoith')
        member = self.club.find_member("Johnny Smoith")
        self.assertEqual(member.name, "Johnny Smoith")

