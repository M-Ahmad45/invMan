import json


class Item:
    def __init__(self, name: str, quantity: int, description=""):
        self.name = name[:21] #only 20 character name
        self.quantity = quantity
        self.description = description[:101] #only 100 character description

    def __str__(self):
        return "{:<20}\t\t{:<4d}\t\t{:<100}\t\t\n".format(self.name, self.quantity, self.description)

    def toDict(self):
        return {"name": self.name, "quantity": self.quantity, "description": self.description}


class Inventory:
    def __init__(self, path=""):
        #id 0 stores the free ids that can be used to store items
        self._free = []
        self.inventory = {0: []}
        self._nextId = 1
        if path:
            self.loadInventory(path)

    def addItem(self, item: Item):
        if self.inventory[0] == []:
            # noinspection PyTypeChecker
            self.inventory[self._nextId] = item
            self._nextId += 1
        else:
            temp = self.inventory[0].pop()
            # noinspection PyTypeChecker
            self.inventory[temp] = item

    def removeItem(self, item_id: int):
        self.inventory[item_id] = None
        self.inventory[0].append(item_id)

    def editItem(self, item_id: int, name="", quantity=-1, description=""):
        if name:
            self.inventory[item_id].name = name
        if quantity >= 0:
            self.inventory[item_id].quantity = quantity
        if description:
            self.inventory[item_id].description = description

    def loadInventory(self, path: str):
        with open(path, 'r') as file:
            self.inventory = json.load(file)
            #convert keys to ints and value to item objects
            temp_dict = dict()
            for key in self.inventory.keys():
                if key != "0":
                    temp_name = self.inventory[key]['name']
                    temp_quantity = self.inventory[key]['quantity']
                    temp_description = self.inventory[key]['description']
                    temp_dict[int(key)] = Item(temp_name, temp_quantity, temp_description)
                else:
                    temp_dict[int(key)] = self.inventory[key].copy()

            self.inventory = temp_dict

    def saveInventory(self, path: str):


        #convert item objects in the dict to strings
        temp = dict()
        temp[0] = self.inventory[0]
        for key in self.inventory.keys():
            if key != 0:
                temp[key] = self.inventory[key].toDict()



        with open(path, 'w') as file:

            json.dump(temp, file, indent=1)

    def isEmpty(self):
        return len(self.inventory.keys()) > 1

    def __str__(self):

        #move inv_str to some other user interface class later
        inv_str = "Showing listing for inventory\n" + "-"*80 + "\n"
        inv_str += "id\t{:<20}\tquantity\t\tdescription\n".format("name")

        # get all item convert them to string and ignore empty ones
        temp = [f"{key}\t"+str(val) for key,val in self.inventory.items() if val!=None]
        temp.pop(0) #get rid of the first list object

        s = "".join(temp)
        return inv_str+s



