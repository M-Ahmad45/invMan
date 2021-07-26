import json


class Item:
    def __init__(self, name: str, quantity: int, description=""):
        self.name = name
        self.quantity = quantity
        self.description = description


class Inventory:
    def __init__(self, path=""):
        #id 0 stores the free ids that can be used to store items
        self.inventory = {0: []}
        self._nextId = 1
        if path:
            self.loadInventory(path)

    def addItem(self, item: Item):
        if self.inventory[0] == []:
            # noinspection PyTypeChecker
            self.inventory[self._nextId] = {"name": item.name,
                                            "quantity": item.quantity,
                                            "description": item.description}
            self._nextId += 1
        else:
            temp = self.inventory[0].pop()
            # noinspection PyTypeChecker
            self.inventory[temp] = {"name": item.name,
                                    "quantity": item.quantity,
                                    "description": item.description}

    def removeItem(self, item_id: int):
        self.inventory[item_id] = {}
        self.inventory[0].append(item_id)

    def loadInventory(self, path: str):
        pass

    def __str__(self):
        inv_str = "Showing listing for inventory\n" + "-"*10 + "\n"

        return self.inventory.__str__()


apple = Item(name="apple",quantity=10)
cpu = Item(name="9900k",quantity=12,description="brand new")
gpu = Item(name="rtx 3080",quantity=100, description="used")
ram = Item(name="Gskkil", quantity=50, description="16gb ddr4 3600mhz dual channel")

inv = Inventory()
inv.addItem(apple)
inv.addItem(cpu)
inv.addItem(gpu)

print(inv)

inv.removeItem(2)
print(inv)

inv.addItem(ram)
print(inv)