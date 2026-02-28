from weaponTable import roll_weapon, weapon_table, weapons
#from mundaneItemTable import *
#from gemstoneTable import *
from itemClass import Item
#from rollGem import print_gem
import random
from decorateItem import *
from weaponClass import Weapon


def main():
    for i in range(10):
        weapon_test = Weapon(weapons["battle_axe"])
        decorate(weapon_test)
        print(weapon_test.description)
    
if __name__ == "__main__":
    main()



    