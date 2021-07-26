import json
from inventory import Inventory, Item

apple = Item(name="apple",quantity=10)
cpu = Item(name="9900k",quantity=12,description="brand new")
gpu = Item(name="rtx 3080",quantity=100, description="used")
ram = Item(name="Gskkil", quantity=50, description="16gb ddr4 3600mhz dual channel")

inv = Inventory()
inv.addItem(apple)
inv.addItem(cpu)
inv.addItem(gpu)

print(inv)

inv.removeItem(3)
print(inv)

inv.addItem(ram)
inv.editItem(1,name="mango")
print(inv)