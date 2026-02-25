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

def is_decorated(percentage):
    roll = random.randint(1, 100)
    if roll <= percentage:
        return True
    return False

def decorate(item):

