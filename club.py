from clubMember import Member
import csv


class Club:
    def __init__(self, club_name, members, file_name=None):
        self.club_name = club_name
        self.members = members
        self.filename = file_name

    def _save_members(self):
        if self.filename:
            Club.write_members(self.filename, self.members)

    @staticmethod
    def load_members(filename):
        members = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                members.append(Member(row[0], row[1], row[2]))
        return members

    @staticmethod
    def write_members(filename, members):
        with open(filename, 'w') as file:
            writer = csv.writer(file, lineterminator="\n")
            for member in members:
                writer.writerow([member.name, member.address, member.phone_number])

    @classmethod
    def from_file(cls, club_name, filename):
        members = cls.load_members(filename)
        return cls(club_name, members, filename)

    def add_member(self, name, address, phone_number):
        self.members.append(Member(name, address, phone_number))
        self._save_members()

    def find_member(self, name):
        for member in self.members:
            if name == member.name:
                return member

    def remove_member(self, name):
        member = self.find_member(name)
        self.members.remove(member)
        self._save_members()

    def new_address(self, name, new_address):
        member = self.find_member(name)
        if member:
            member._address = new_address
        self._save_members()

    def new_phone_number(self, name, new_phone_number):
        member = self.find_member(name)
        if member:
            member._phone_number = new_phone_number
        self._save_members()

    def change_name(self, old_name, new_name):
        member = self.find_member(old_name)
        if member:
            member._name = new_name
        self._save_members()

    def return_members(self):
        return list(self.members)


