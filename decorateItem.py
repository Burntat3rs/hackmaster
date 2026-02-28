import random
from rollGem import roll_gem
from genericFunctions import a_or_an

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

shapes = [("bear claw", "bear claws"), ("skeletal hand", "skeletal hands"), ("skull", "skulls"), ("complex geometric pattern", "complex geometric patterns"),
("runic poem", "runic poems"), ("grotesque snarling face", "grotesque snarling faces"), ("giant insect claw", "giant insect claws"), ("gnawing termite", "swarming termites"),
("serpent scale", "serpent scales"), ("leaping wolf", "leaping wolves"), ("beehive", "beehives"), ("tiny thorn", "tiny thorns"), ("stud", "studs"), ("writhing snake", "writhing snakes"),
("raven skull", "raven skulls"), ("spiny sea urchin", "spiny sea urchins"), ("ball of fire", "balls of fire"), ("blazing sun with a placid face", "blazing suns with placid faces"),
("shard of ice", "shards of ice"), ("sneering rat", "sneering rats"), ("blowing wind", "blowing winds"), ("eagle's head", "eagles' heads"), ("forked demonic tongue", "forked demonic tongues"),
("stinging wasp", "stinging wasps"), ("snarling ape", "snarling apes"), ("clenched fist", "clenched fists"), ("blazing sun", "blazing suns"), ("ox head", "ox heads"), ("dodecahedron", "dodecahedrons"),
("grinning skull", "grinning skulls"), ("scorpion stinger", "scorpion stingers"), ("eagle with spread wings", "eagles with spread wings"), ("full moon", 'full moons'), ("crescent moon", "crescent moons"),
("waxing moon", "waxing moons"), ("waning moon", "waning moons"), ("jawless skull", "jawless skulls"), ("large eye", "large eyes"), ("many pronged star", "many pronged stars"), ("curled hedgehog", "curled hedgehogs"),
("bracing pikeman", "phalanx of pikemen"), ("terrible beak", "terrible beaks"), ("gauntlet grasping a knife", "gauntlets grasping knives"), ("lightning bolt", "lightning bolts"),
("twisting narwhal horn", "twisting narwhal horns"), ("black tower", "black towers"), ("dragon's mouth", "dragons' mouthes"), ("spined lizard", "spined lizards"), ("warrior with his back to a wall", "three warriors back to back"),
("a dragon", "twin dragons"), ("thorny rose", "thorny roses"), ("cresting wave", "cresting waves"), ("perching vulture", "perching vultures"), ("heron's curved neck", "herons' curved necks"),
("dragon's curved neck", "dragons' curved necks"), ("a finger in the ass", "two fingers in the ass"), ("clawed hand of a hag", "clawed hands of a hag coven"), ("thorny bramble", "thorny vines of a twisting bramble"),
("scorpion", "scorpions"), ("weeping demon", "weeping demons"), ("roaring bonfire", "roaring bonfires"), ("comet with a streaking tail", "comets with streaking tails"),
("manticore's open maw", "manitcores' open maws"), ("sunburst", "sunbursts"), ("prowling predatory animal", "prowling predatory animals"), ("vicious ocean wave", "waves crashing on rocks"),
("pouncing lion with claws outstretched", "pouncing lions with claws outstretched"), ("intertwining knot", "intertwining knots"), ("galloping horse", "galloping horses"), ("grinning face of a dragon", "several dragons' grinning faces"),
("gold and jewel encrusted crown", "gold and jewel encrusted crowns"), ("coiled tentacle", "coiled tentacles"), ("trefoil leaf", "trefoil leaves"), ("bat with outstretched wings", "bats with outstretched wings"),
("twisting conch shell", "twisting conch shells"), ("raging brazier", "raging braziers"), ("wyvern head", "wyvern heads"), ("eyes peering from dark shadows", "many eyes peering from dark shadows"),
("cruel talon", "cruel talons"), ("grasping skeleton", "grasping skeletons"), ("leaping flame", "leaping flames"), ("biting eel", "biting eels"), ("coiling centipede", "coiling centipedes"), ("snarling ghoul", "snarling ghouls"),
("staring owl", "staring owls"), ("dwarven rune", "dwarven runes"), ("elvish pictograph", "elvish pictographs"), ("slithering snake", "slithering snakes"), ("tree branch", "tree branches"), ("bull's horns", "horns of bulls"),
("blazing sun", "blazing suns"), ("charging cavalryman", "charging cavalry"), ("darting fox", "darting foxes"), ("coiling dragon", "coiling dragons"), ("black anvil", "black anvils"), ("mist shrouded mountain", "mist shrouded mountains"),
("rushing river", "rushing rivers"), ("grotesque gargoyle", "grotesque gargoyles"), ("scene of autumn", "scenes of autumn"), ("biting fly", "biting flies"), ("towering tree", "towering trees"),
("spitting hydra", "spitting hydras")]

verbs = ["grasping", "holding", "eating", "devouring", "battling", "shaping", "forging", "hunting",
"vomiting", "saving", "defeating", "emanating from", "leaping toward", "fleeing from", "running toward",
"releasing", "protecting", "carving a picture of", "swatting"]

decorate_methods = ["laquering", "etching", "engraving", "carving", "cast"]

gem_methods = ["encrusted", "set",]

def check_for_fully_decorated(item):
    return all(option in item.description for option in decoratable_features[item.type])
        

def roll_feature(item):
    feature = random.choice(decoratable_features[item.type])
    
    while feature in item.description:
        feature = random.choice(decoratable_features[item.type])

    return feature

def roll_method():
    return random.choice(decorate_methods)

def roll_verb():
    return random.choice(verbs)

def roll_shape():
    return check_for_pluralized_shape(random.choice(shapes))

def roll_material():
    return random.choice(materials)


    


def is_decorated(percentage):
    roll = random.randint(1, 100)
    if roll <= percentage:
        return True
    return False

def roll_gem_method():
    return random.choice(gem_methods)


def gem_decoration(item, feature=None):
    if check_for_fully_decorated(item):
        return
    
    if feature == None:
        feature = roll_feature(item)

    gem = roll_gem()

    method = roll_gem_method()

    if method == "set":
        item.description = item.description + f"The {feature} is set with {gem.description} colored {check_for_pluralize(gem.name)}. "
    elif method == "encrusted":
        item.description = item.description + f"The {feature} is encrusted with many {gem.description} colored {gem.name}s. "
    
    return






def material_decoration(item, feature=None):
    if check_for_fully_decorated(item):
        return

    if feature == None:
        feature = roll_feature(item)

    material = roll_material()

    item.description = item.description + f"The {feature} is made from {material}. "

def shape_decoration(item, feature=None, method=None):
    shape = roll_shape()

    if check_for_fully_decorated(item):
        return

    if feature == None:
        feature = roll_feature(item)
        
    if method == None and is_decorated(25) == True:
        method = roll_method()
        item.description = item.description + f"The {feature} has {a_or_an(method)} {method} on it in the shape of {shape}. "
        item.description = verb_decoration(item.description, 25)
        return
    
    item.description = item.description + f"The {feature} is in the shape of {shape}. "
    item.description = verb_decoration(item.description, 25)

    return
    

def verb_decoration(str, chance):
    if is_decorated(chance) == False:
        return str
    verb = roll_verb()
    shape = roll_shape()
    #str slice to remove period and space
    return str[0:-2] + f" {verb} {shape}. "


def choose_decoration_type():
    return random.choice(decorate_funcs)


#tuple of two options 0 = singular, 1 = plural
#then returns the proper structure

def check_for_pluralize(str):
    if is_decorated(25):
        return str + 's'
    return str

def check_for_pluralized_shape(tuple):
    if is_decorated(50) == True:
        return tuple[1]
    return f"{a_or_an(tuple[0])} {tuple[0]}"

def decorate(item, x=10):

    check_for_decorate = is_decorated(x)

    if not check_for_decorate:
        return
    else:
        func = choose_decoration_type()
        func(item)
        decorate(item, 50)

        
decorate_funcs = [shape_decoration, material_decoration,gem_decoration]
