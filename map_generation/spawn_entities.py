import entities.mobs as mobs
import entities.items as items
import dice
from random import choice
from inspect import getmembers, isclass

def get_mob_list():
    mob_list = [mobs.Mob_Goblin, mobs.Mob_Ant, mobs.Mob_Blob, mobs.Mob_Cockatrice]
    #mob_list = [list(i[1][-len(i[0]):-3] for i in getmembers(mobs, isclass) if i[0][:3] == "Mob"]
    #mob_list = getmembers(mobs, isclass)
    #print(mob_list[0][0][:3])
    return mob_list

def get_item_list():
    item_list = [items.Health_Pot]
    return item_list

def choose_item_to_spawn():
    potential_items = get_item_list()
    item_spawned = False
    while not item_spawned:
        item = choice(potential_items)
        roll = dice.roll_dice(1, 100)[0]
        item_spawned = [0,1][roll <= item(0,0).components["item"].spawn_chance]
    return item

def choose_mob_to_spawn():
    potential_mobs = get_mob_list()
    mob_spawned = False
    while not mob_spawned:
        mob = choice(potential_mobs)
        roll = dice.roll_dice(1, 100)[0]
        mob_spawned = [0,1][roll <= mob(0,0).components["fighter"].spawn_chance]
    return mob
        