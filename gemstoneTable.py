import random
from weaponTable import split_index_from_table


#type, color, value
common_gems = [("azurite", "vibrant blue", 10), ("banded agate", "pink", 10),
("blue quartz", "pale blue", 10), ("eye agate", "reddish pink", 10), ("hematite", "rust", 10),
("lapis lazuli", "royal blue", 10), ("malachite", "teal", 10), ("moss agate", "white with green veins", 10),
("obsidian", "black", 10), ("rhodochrosite", "blood red", 10), ("tiger eye", "rich layers of brown", 10),
("turquoise", "turquoise", 10)
] 

uncommon_gems = [("bloodstone", "black with blood red flecks", 50), ("carnelian", "orangish red", 50),
("chalcedony", "pale purple", 50), ("chrysoprase", "seafoam green", 50), ("citrine", "pale gold", 50),
("jasper", "deep red with black veins", 50), ("moonstone", "bone white with bluish center", 50),
("onyx", "deep black", 50), ("rock crystal", "clear", 50), ("sardonyx", "bands of red", 50),
("smoky quartz", "hazy grey", 50), ("rose quartz", "gentle pink", 50)
] 

precious_gems = [("amber", "honey yellow", 100), ("alexandrite", "green and purple", 100),
("amethyst", "vibrant purple", 100), ("chrysoberyl", "burnished gold", 100), ("coral gemstone", "red", 100),
("garnet", "deep orange", 100), ("jade", "pale green", 100), ("jet", "pure black", 100),
("pearl", "pearlescent white", 100), ("spinel", "lilac", 100), ("tourmaline", "green and pink", 100),
("zircon", "bright blue", 100) 
] 

rare_gems = [("aquamarine", "pale blue", 500), ("garnet", "reddish orange", 500), ("pearl", "pearlescent black", 500),
("peridot", "olive green", 500), ("spinel", "dark pink", 500), ("topaz", "golden yellow", 500)
] 

super_rare_gems = [("black opal", "dark irridescent", 1000), ("emerald", "bluish green", 1000), ("fire opal", "orangish red", 1000),
("garnet", "dark red", 1000), ("opal", "white irridescent", 1000), ("corrundum", "vibrant purple", 1000),
("sapphire", "yellow", 1000), ("sapphire", "royal blue", 1000), ("ruby", "red with white star shaped veins", 1000),
("sapphire", "purplish blue with white star shaped veins", 1000)
]

ultra_rare_gems = [("sapphire", "deep black", 5000), ("diamond", "clear white", 5000), ("jacinth", "fire red", 5000),
("sapphire", "green", 5000), ("ruby", "vibrant red", 5000)
]


#category, randomize weight
gemstones_category = [(common_gems, 500), (uncommon_gems, 100),
(precious_gems, 50), (rare_gems, 10), (super_rare_gems, 5),
(ultra_rare_gems, 1)
]

# size, randomize weight, value modifier
gem_size = [("tiny", 8, .125), ("very small", 16, .25), ("small", 32, .5),
    ("average", 64, 1.0), ("large", 16, 2.0), ("very large", 8, 4.0),
    ("huge", 4, 8.0), ("massive", 2, 16.0), ("gargantuan", 1, 32.0)
]

#quality goes between -+ 50%
def get_gem_quality():
    return random.uniform(-.5, .5)

def print_gem(table):
    for tup in weapon_table:
        print(f"Gem: {tup[0]}    Weight:{tup[1]}\n")

def get_table_category(table):
    
    chosen_category = random.choices(
        population=split_index_from_table(table, 0),
        weights=split_index_from_table(table, 1)
    )
    
    return chosen_category[0]
