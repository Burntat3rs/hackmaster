
#has a name and weight value for randomization
#weight is based off of table GMG, pg245, Table 13.1
weapon_table = [("battle_axe", 42), ("hand_axe", 15), ("club", 6),
("dagger", 54), ("flail", 31), ("knife", 23), ("lance", 8), ("mace", 39),
("morning_star", 15), ("military_pick", 12), ("bardiche", 17),
("bec_de_corbin", 6), ("bill_guisarme", 5), ("fauchard", 2),
("fauchard_fork", 2), ("military_fork", 1), ("glaive", 19),
("glaive_guisarme", 12), ("guisarme", 2), ("guisarme_voulge", 4),
("halberd", 19), ("partisan", 6), ("pike", 7), ("ranseur", 1),
("short_spear", 23), ("spear", 39), ("spetum", 15), ("trident", 8),
("voulge", 19), ("scourge", 15), ("scythe", 6), ("staff", 39),
("broadsword", 42), ("great_sword", 31), ("longsword", 56),
("sabre", 22), ("scimitar", 23), ("short_sword", 39),
("two_handed_sword", 15), ("warhammer", 39), ("great_warhammer", 12),
("throwing_axe", 16), ("heavy_crossbow", 15), ("light_crossbow", 39),
("javelin", 45), ("throwing_knife", 15), ("longbow", 23),
("shortbow", 39), ("sling", 18)
]


weapons = {
    "battle_axe":  {
        "name": "Battle Axe",
        "type": "axe",
        "value": (5, "sp"),
        "weight": 3.5,
        "damage": [(4, 3, True, 0)], #(num of dice, die size, penetrates?, additional damage)
        "shield_damage": [(3, 3, True, 0)],
        "damage_type": "hacking",
        "speed": 12,
        "jab_speed": None,
        "jab_damage": None,
        "size": "medium",
        "reach": 3.0,
        "skill": "low",
        "strength_requirement": 10,
        "max_range": None,
        "range_step": None,
        "can_dismount": False,
        "ignore_armor": False,
        "can_set_for_charge": False,
        "defense_bonus": False,
        "phalanx_rank": None
    },
    "hand_axe": {
        "name": "Hand Axe",
        "type": "axe",
        "value": (3, "sp"),
        "weight": 2,
        "damage": [(1, 4, True, 0), (1, 6, True, 0)],
        "shield_damage": [(1, 6, True, 0)],
        "damage_type": "hacking",
        "speed": 8,
        "jab_speed": None,
        "jab_damage": None,
        "size": "small",
        "reach": 1.5,
        "skill": "low",
        "strength_requirement": 6,
        "max_range": None,
        "range_step": None,
        "can_dismount": False,
        "ignore_armor": False,
        "can_set_for_charge": False,
        "defense_bonus": False,
        "phalanx_rank": None
    },
}


#prints the list
def print_weapon_list(table):
    for tup in weapon_table:
        print(f"Weapon: {tup[0]}    Weight:{tup[1]}\n")

def roll_weapon(rolls=1):
    random_weapons = random.choices(
        population=split_index_from_table(weapon_table, 0),
        weights=split_index_from_table(weapon_table, 1),
        k=rolls
    )
    return random_weapons