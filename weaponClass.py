from itemClass import Item

class Weapon(Item):
    def __init__(self, name, description, value, quality, item_type="weapon"):
        item.__init__(self, name, item_type)