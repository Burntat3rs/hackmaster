import random
from gemstoneTable import gemstones_category

decoratable_features = {
    "axe": ["handle", "haft", "head", "blade"],
    "blade": ["pommel", "grip", "guard", "blade"],
    "bow": ["handle", "limb", "string"],
    "blunt": ["handle", "haft", "head"],
    "polearm":["haft", "head", "blade"],
    "crossbow": ["trigger", "stock", "lath", "stirrup", "string"],
}

materials = ["steel", "gold", "silver", "platinum", "bronze", "copper", "iron",
"troll bone", "hill giant bone", "bright coral", "black iron", "burnished gold",
"burnished bronze", "tarnished copper", "tarnished brass", "rusted iron", "crystal", "ox bone",
"chitin", "wood", "white gold", "lead", "pewter", "stone"]

shapes = ["bear claw", "skeletal hands", "skull", "complex geometric patterns",
"runic poetry", "grotesque snarling faces", "giant insect claws", "swarming termites",
"scales", "leaping wolves", "beehive", "tiny thorns", "studs", "writhing snakes",
"raven skull", "spiny sea urchin", "ball of fire", "blazing sun with a placid face",
"shard of ice", "sneering rat", "blowing wind", "eagle's head", "forked demonic tongue",
"stinging wasp", "snarling ape", "clenched fist", "blazing sun", "ox head", "dodecahedron",
"grinning skull", "scorpion stinger", "eagle with spread wings", "full moon", "crescent moon",
"waxing moon", "waning moon", "jawless skull", "large eye", "many pronged star", "curled hedgehog",
"phalanx of pikemen", "terrible beak", "gauntlet grasping a knife", "lightning bolt",
"twisting narwhal horn", "black tower", "dragon's mouth", "spined lizard", "three warriors back to back",
"twin dragons", "thorny rose", "cresting wave", "perching vulture", "heron's curved neck",
"dragon's curved neck", "two fingers in the ass", "clawed hand of a hag", "thorns of a twisting bramble",
"scorpions", "weeping demon", "black smoke from a roaring bonfire", "two comets with streaking tails",
"manticore's open maw", "sunbursts", "predatory animals prowling in a dense jungle", "waves crashing on rocks",
"pouncing lion with claws outstretched", "intertwining knots", "galloping horse", "grinning face of a dragon",
"gold and jewel encrusted crown", "coiled tentacles", "three bladed leaves", "bat with outstretched wings",
"twisting conch shell", "flames from a raging brazier", "wyvern head", "eyes peering from dark shadows",
"cruel talons", "grasping skeletons", "leaping flames", "biting eel", "coiling centipedes", "snarling ghoul",
"staring owl", "dwarven runes", "elvish script", "slithering snakes", "tree branches", "horns of a bull",
"blazing sun", "charging cavalry", "darting foxes", "coiling dragons", "black anvil", "mist shrouded mountain",
"rushing rivers", "grotesque frowning gargoyle", "scenes of autumn", "lightning bolts", "biting flies", "towering trees",
"spitting hydra"]

verbs = ["grasping", "holding", "eating", "devouring", "battling", "shaping", "forging", "hunting",
"vomiting", "saving", "defeating", "emanating from", "leaping toward", "fleeing from", "running toward",
"releasing", "protecting", "carving a picture of", "swatting"]

decorate_methods = ["laquering", "etching", "engraving", "carving", "cast"]

def roll_feature(item):
    return random.choice(decoratable_features[item.type])

def roll_method():
    return random.choice(decorate_methods)

def roll_verb():
    return random.choice(verbs)

def roll_shape():
    return random.choice(shapes)

def roll_material():
    return random.choice(materials)

def is_decorated(percentage):
    roll = random.randint(1, 100)
    if roll <= percentage:
        return True
    return False

def material_decoration(item, feature=None):
    material = roll_material()
    
    if feature None:
        feature = roll_feature(item)

    item.description = item.description + f"The {feature} is made from {material}"

def shape_decoration(item, feature=None, method=None):
    shape = roll_shape()

    if feature None:
        feature = roll_feature(item)
        
    if method == None and is_decorated(25) == True:
        method = roll_method()
        item.description = item.description + f"The {item.name}'s {feature} has {a_or_an(method)} {method} on it in the shape of {shape}."
        item.description = verb_decoration(item.description)
        return
    
    item.description = item.description + f"The {item.name}'s {feature} is in the shape of {shape}"
    item.description = verb_decoration(item.description)

    return
    

def verb_decoration(str):
    if is_decorated(25) == False:
        return str
    verb = roll_verb
    shape = roll_shape
    #str slice to remove period
    return str[0:-1] + f"{verb} {a_or_an(shape_two)} {shape_two}."


def choose_decoration_type():
    pass

def pluralize(str):
    if str[-1:] not 's':
        return str + 's'
    return

def decorate(item):

    if not is_decorated(10):
        return
    else:
        

