from itemClass import Item

class Weapon(Item):
    def __init__(self, dict):
        super().__init__(dict["name"], dict["type"])
        self.value = dict["value"]
        self.weight = dict["weight"]
        self.damage = dict["damage"]
        self.shield_damage = dict["shield_damage"]
        self.damage_type = dict["damage_type"]
        self.speed = dict["speed"]
        self.jab_speed = dict["jab_speed"]
        self.jab_damage = dict["jab_damage"]
        self.size = dict["size"]
        self.reach = dict["reach"]
        self.skill = dict["skill"]
        self.strength_requirement = dict["strength_requirement"]
        self.max_range = dict["max_range"]
        self.range_step = dict["range_step"]
        self.can_dismount = dict["can_dismount"]
        self.ignore_armor = dict["ignore_armor"]
        self.can_set_for_charge = dict["can_set_for_charge"]
        self.defense_bonus = dict["defense_bonus"]
        self.phalanx_rank = dict["phalanx_rank"]

        self.description = f"This is a {self.name}. "



