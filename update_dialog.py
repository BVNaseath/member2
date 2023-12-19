import tkinter as tk
from tkinter import simpledialog

class UpdateDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title, name=None, address=None, phone=None):
        self.name = name
        self.address = address
        self.phone = phone
        super().__init__(parent, title)

    def body(self, frame):
        self.member_name = tk.Label(frame, width=25, text="Member name")
        self.member_name.pack()
        self.member_name_box = tk.Entry(frame, width=25)
        if self.name is not None:
            self.member_name_box.insert(0, self.name)
        self.member_name_box.pack()

        self.member_address_label = tk.Label(frame, width=25, text="Address")
        self.member_address_label.pack()
        self.member_address_box = tk.Entry(frame, width=25)
        if self.address is not None:
            self.member_address_box.insert(0, self.address)
        self.member_address_box.pack()

        self.member_phone_label = tk.Label(frame, width=25, text="Phone Number")
        self.member_phone_label.pack()
        self.member_phone_box = tk.Entry(frame, width=25)
        if self.phone is not None:
            self.member_phone_box.insert(0, self.phone)
        self.member_phone_box.pack()

        return frame

    def ok_pressed(self):
        self.name = self.member_name_box.get()
        self.address = self.member_address_box.get()
        self.phone = self.member_phone_box.get()
        self.destroy()

    def cancel_pressed(self):
        self.destroy()


    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

