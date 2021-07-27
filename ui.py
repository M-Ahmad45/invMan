from inventory import Inventory


class UI:
    def __init__(self):
        self.inventory = Inventory()

    def menu(self):
        print("Hello and welcome to Inventory manager. Please select and option:")
        print("1.Load an inventory file from disk\t2.Save inventory to disk")
        print("3.Create an inventory manually")

    def __load(self):
        pass

    def __save(self):
        pass

    def __addItem(self):
        pass

    def __removeItem(self):
        pass

    def __editItem(self):
        pass
