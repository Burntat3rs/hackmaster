from genericFunctions import a_or_an

class Item():
    def __init__(self, name, item_type="generic"):
        self.name = name
        self.type = item_type

    def print_self(self):
        print(f"{self.name} is a kind of {self.item_type}")


