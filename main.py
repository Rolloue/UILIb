import os
import sys
import tkinter
from tkinter import filedialog
import rich

class FileSelect:
    def __init__(self, message, file_type, base_dir = None):
        self.base_dir = base_dir
        self.message = message
        self.file_type = file_type
    def select(self):
        while True:
            response = input(self.message)
            if response == "exit":
                return 1
            file = filedialog.askopenfilename(initialdir = self.base_dir, filetypes = self.file_type)
            if file != "":
                break
        return file
class Entry:
    def __init__(self, text, option, base_dir = None, default = None, required = False):
        self.text = text
        self.option = option
        match option:
            case "file-select":
                self.base_dir =
    def __str__(self):
        return self.text
class Menu:
    def __init__(self, entries):
        self.availOptions = ["file-select", "boolean", "multichoice", "freeform"]
        self.entries = entries
        self.entries.options = []
        self.textColor = "red"
        self.message = "Please select an option: "
    def setOption(self, entry, option):
        if self.entries.length < entry:
            raise IndexError("Entry does not exist")

        found = False
        for i in range(len(self.availOptions)):
            if option == self.availOptions[i]:
                found = True
                break
        if not found:
            raise ValueError("Invalid option")

        self.entries.options[entry - 1] = option

    def execChoice(self, choice):

    def show(self):
        while True:
            for i in range(len(self.entries)):
                print(f"{i + 1}. {self.entries[i]}")
            selection = input(self.message)
            if (int(selection) > 0) & (int(selection) <= len(self.entries)):
                break
        self.execChoice(int(selection))