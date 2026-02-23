
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

blade_table = [
]


#prints the list
def print_weapon_list(table):
    for tup in weapon_table:
        print(f"Weapon: {tup[0]}    Weight:{tup[1]}\n")

