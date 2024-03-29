def add_arrows(entity, args):
    """
    Add arrows to the entities equipment
    """
    arrow_count = args.get("arrow_count")
    equipment_component = entity.components.get("equipment")
    if equipment_component:
        equipment_component.equipment["arrows"] += arrow_count
        return True
    else:
        return False

def toggle_equip(entity, args):
    """
    Toggle whether an equipment piece is equipped
    """
    equipment_component = entity.components.get("equipment")
    slot = args.get("slot")
    item = args.get("item")
    if equipment_component:
        was_equipped = dequip(equipment_component.equipment, slot, item)
        if not was_equipped:
            equip(equipment_component.equipment, slot, item)
        return True
    return False

def equip(equipment_list, slot, item):
    """
    Equip an equipment piece
    """
    equipment_list[slot] = item
    return True

def dequip(equipment_list, slot, item):
    """
    Dequip an equipment piece
    """
    if equipment_list[slot] == item:
        equipment_list[slot] = None
        return True
    else:
        return False

def decrease_hunger(entity, args):
    hunger_decrease_ratio = args.get("hunger_decrease_ratio")
    hunger_component = entity.components.get("hunger")
    if hunger_component is not None:
        hunger_component.turns -= hunger_component.turns_to_starve * hunger_decrease_ratio
        return True
    else:
        return False

def heal_entity(entity, args):
    heal_amount = args.get("heal_amount")
    if heal_amount is not None and entity.components.get("fighter") and entity.components["fighter"].hp < entity.components["fighter"].max_hp:
        fighter = entity.components["fighter"]
        fighter.hp += heal_amount
        if fighter.hp > fighter.max_hp:
            fighter.hp = fighter.max_hp
        return True
    else:
        return False

def damage_entity(entity, args):
    args = {"heal_amount": args.get("damage_amount")}
    return heal_entity(entity, args)

def increase_strength(entity, args):
    increase_amount = args.get("strength_increase")
    if increase_amount is not None and entity.components.get("fighter"):
        fighter = entity.components["fighter"]
        fighter.strength += increase_amount
        return True
    else:
        return False

def increase_defense(entity, args):
    increase_amount = args.get("defense_increase")
    if increase_amount is not None and entity.components.get("fighter"):
        fighter = entity.components["fighter"]
        fighter.defense += increase_amount
        return True
    else:
        return False

def increase_accuracy(entity, args):
    increase_amount = args.get("accuracy_increase")
    if increase_amount is not None and entity.components.get("fighter"):
        fighter = entity.components["fighter"]
        fighter.accuracy += increase_amount
        return True
    else:
        return False

def increase_dexterity(entity, args):
    increase_amount = args.get("dexterity_increase")
    if increase_amount is not None and entity.components.get("fighter"):
        fighter = entity.components["fighter"]
        fighter.dexterity += increase_amount
        return True
    else:
        return False

def increase_intelligence(entity, args):
    increase_amount = args.get("intelligence_increase")
    if increase_amount is not None and entity.components.get("fighter"):
        fighter = entity.components["fighter"]
        fighter.intelligence += increase_amount
        return True
    else:
        return False

def increase_max_hp(entity, args):
    increase_amount = args.get("max_hp_increase")
    if increase_amount is not None and entity.components.get("fighter"):
        fighter = entity.components["fighter"]
        fighter.max_hp += increase_amount
        return True
    else:
        return False
