from inventory import Inventory
import questionary as q
import os
import sys


def clrscr():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win32"):
        os.system("cls")
    elif sys.platform.startswith("darwin"):
        os.system("clear")


class UI:
    def __init__(self):
        self.inventory = Inventory()
        #menu option strings
        self.__options = {"inv_dir": "inventories",
                          "inv_file": "",
                          "load": "Load inventory",
                          "create": "Create inventory",
                          "add": "Add Item to inventory",
                          "remove": "Remove Item from inventory",
                          "edit": "Edit Item in inventory",
                          "save": "Save inventory",
                          "show": "Show inventory",
                          "clrscr": "Clear screen",
                          "quit": "Quit Inventory Manager",
                          "quit_ws": "Quit without saving",
                          "save_q": "Save and quit"}
        self.u_changes = False #unsaved changes

    def menu(self):
        while True:
            c = q.select("please select", choices=[self.__options["load"],
                                                   self.__options["create"],
                                                   self.__options["quit"]
                                                   ]).ask()

            if c == self.__options["load"]:
                self.__load()
            elif c == self.__options["create"]:
                self.__create()
            elif c == self.__options["quit"]:
                clrscr()
                break

    def editor_menu(self):
        while True:
            c = q.select("please select", choices=[self.__options["add"],
                                                   self.__options["remove"],
                                                   self.__options["edit"],
                                                   self.__options["save"],
                                                   self.__options["clrscr"],
                                                   self.__options["quit"],
                                                   self.__options["show"]
                                                   ]).ask()
            if c == self.__options["add"]:
                self.__addItem()
            elif c == self.__options["remove"]:
                self.__removeItem()
            elif c == self.__options["edit"]:
                self.__editItem()
            elif c == self.__options["save"]:
                self.__save()
            elif c == self.__options["clrscr"]:
                clrscr()
            elif c == self.__options["show"]:
                self.__showInventory()
            elif c == self.__options["quit"]:
                if self.u_changes:
                    clrscr()
                    c = q.select("You have unsaved changes what would you like to do?", choices=[
                        self.__options["quit_ws"],
                        self.__options["save_q"]
                    ]).ask()
                    if c == self.__options["quit_ws"]:
                        break
                    elif c == self.__options["save_q"]:
                        self.__save()
                        break
                else:
                    clrscr()
                    break

    def __load(self):
        print(os.getcwd())
        if not os.getcwd().endswith(self.__options["inv_dir"]):
            os.chdir(self.__options["inv_dir"])
        file = q.path("Please select json inventory file").ask()
        if not file:
            clrscr()
            print("No file selected")
            return
        try:
            self.inventory.loadInventory(file)
            self.__options["inv_file"] = file
            self.editor_menu()
        except FileNotFoundError:
            input("File Not Found. Press Enter to continue")

    def __save(self):
        if not os.getcwd().endswith(self.__options["inv_dir"]):
            os.chdir(self.__options["inv_dir"])
        self.inventory.saveInventory(self.__options["inv_file"])
        self.u_changes = False

    def __addItem(self):
        name = input("Please enter item name:")
        if name:
            try:
                quantity = int(input("Please enter item quantity:"))
                description = input("Please enter item description:")
                self.inventory.addItem(name=name, quantity=quantity, description=description)
                print("Item added successfully.")
                self.u_changes = True
            except TypeError:
                input("Please only enter integers. Press Enter to continue")
        else:
            input("Empty Name not allowed. Press Enter to continue")

    def __removeItem(self):
        try:
            item_id = int(input("Enter id:"))
            if self.inventory.removeItem(item_id):
                print("Item Removed Successfully")
                self.u_changes = True
            else:
                input("Invalid ID. Press Enter to continue")
        except TypeError:
            input("Please only enter integers. Press Enter to continue")

    def __editItem(self):
        try:
            item_id = int(input("Enter id:"))
            clrscr()
            temp = self.inventory.atId(item_id)
            if temp == {}:
                input("Invalid ID. Press Enter to continue")
                return
            name = temp["name"]
            quantity = temp["quantity"]
            description = temp["description"]
            print(f"Editing id:{item_id}\t name:{name}\t quantity:{quantity}\t description:{description}")
            print("Leave the option empty if you do not want to modify")
            name = input("New Name:")
            quantity = input("New Quantity:")
            description = input("New Description:")

            if quantity.isdigit():
                quantity = int(quantity)
            else:
                quantity = -1
            self.inventory.editItem(item_id, name, quantity, description)
            self.u_changes = True
            input("Changes applied press enter to continue")
            clrscr()

        except TypeError:
            input("Please only enter integer as id. Press Enter to continue")

    def __showInventory(self):
        clrscr()
        print(self.inventory)
        input("\nPress enter to continue")

    def __create(self):
        file = input("Enter Inventory name:")
        self.__options["inv_file"] = file+".json"
        self.editor_menu()
