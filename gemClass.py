from itemClass import Item
from genericFunctions import a_or_an

class Gem(Item):
    def __init__(self, name, description, base_value, size, quality, item_type="gem"):
        Item.__init__(self, name, item_type)
        self.description = description
        self.base_value = base_value
        self.size = size
        self.quality = quality
        self.item_type = item_type
        self.quality_description = self.set_descriptive_quality()
        self.true_value = (base_value * (1 + quality)) * size[2]

    def print_self(self):
        print(f"This is {a_or_an(self.name[0])} {self.name} {self.item_type}.")
        print(f"It is {a_or_an(self.size[0])} {self.size[0]}, {self.description} colored {self.item_type}")
        print(f"It's cut is {self.quality_description}. It's value is {int(self.true_value)} SP\n")

    def set_descriptive_quality(self):
        
        if self.quality < -.25:
            return "bad"
        elif self.quality < -.15:
            return "poor"
        elif self.quality < 0:
            return "below average"
        elif self.quality < .16:
            return "middling"
        elif self.quality < .26:
            return "fair"
        else:
            return "good"


