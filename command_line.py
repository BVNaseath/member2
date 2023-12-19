from club import *
from clubMember import *
import csv

def main():
    club = Club.from_file("TSA", "members.csv")
    again = "Y"
    while again != "N":
        print('''
        1. List all members
        2. Add a member
        3. Remove a member
        4. Update a member's name
        5. Update a member's address
        6. Update a member's phone number
        7. Give (or indicate) a date, name (or indicate the member) and if the member is present.
        8. List all members, and their attendance on a given date.
        9. List all members absent on a given date.
        10. List all members present on a given date.
        ''')

        again = input("Pick the number of what you want to do or type N to finish.")

        match again:
            case "1":
                list_members(club)
            case "2":
                add_member()
            case "3":
                remove_member()
            case "4":
                update_name()
            case "5":
                update_address()
            case "6":
                update_phone_number()
            case "7":
                date_name_present()
            case "8":
                list_attendance()
            case "9":
                list_absent()
            case "10":
                list_present()


    def list_members():
        with open("members.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row} \n")

    def add_member():
        new_member = input("Type in your new member")
        with open("members.csv", 'a') as file:
            file.write(new_member)
