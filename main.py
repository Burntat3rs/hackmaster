from weaponTable import *
from mundaneItemTable import *
from gemstoneTable import *
from itemClass import *
import random


def main():
    random_weapons = random.choices(
        population=split_index_from_table(weapon_table, 0),
        weights=split_index_from_table(weapon_table, 1),
        k=10
    )
    count = 1
    for item in random_weapons:
        print(f"{count}. {item}")
        count += 1

    print("\n\n")

    roll_gems(5)

if __name__ == "__main__":
    main()



    