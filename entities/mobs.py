from components.fighter import *
from components.ai import *
from components.inventory import *
from components.equipment import *
from components.level import *
from components.hunger import Hunger
from render.render_classes import Render_Order
from entities.entity_classes import Entity

class Player(Entity):
    # Initialization of player entity
    def __init__(self, x, y, name, fighter_class):
        # Inializing the players components
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 100, lvl_up_factor = 2)
        inventory_component = Inventory(26)
        ai_component = Base_AI()
        equipment_component = Equipment()
        hunger_component = Hunger(turns_to_starve = 1000)
        components_dict = {"ai": ai_component, "inventory": inventory_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component, "hunger": hunger_component}

        # Composing entity
        super().__init__(x, y, name, "@", "white", "This is you, the player.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

    # Move player and adjust offset accordingly
    def move(self, dx, dy):
        self.components["ai"].move(dx, dy)
        self.x_offset -= dx
        self.y_offset -= dy

class Mob_Goblin(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("goblin", strength = 3, defense = 1, accuracy = 2, intelligence = 0, dexterity = 0, max_hp = 20)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 2)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "goblin", "g", "green", "An ugly green goblin.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Ant(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("ant", strength = 1, defense = 1, accuracy = 4, intelligence = 0, dexterity = 0, max_hp = 5)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 1)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "ant", "a", "brown", "A large ant.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Blob(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 3
    def __init__(self, x, y):
        fighter_class = Fighter_Class("blob", strength = 3, defense = 2, accuracy = 2, intelligence =0, dexterity = 0, max_hp = 10)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 2)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "blob", "b", "cyan", "A gooey blob.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Cockatrice(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 10
    def __init__(self, x, y):
        fighter_class = Fighter_Class("cockatrice", strength = 3, defense = 4, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 15)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 3)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "cockatrice", "c", "yellow", "Dangerous bird.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Wolf(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 5
    def __init__(self, x, y):
        fighter_class = Fighter_Class("wolf", strength = 4, defense = 2, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 25)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 3)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "wolf", "d", "brown", "A ferocious wolf.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Floating_Eye(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("floating eye", strength = 1, defense = 1, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 40)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 2)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "floating eye", "e", "green", "A strange floating eye.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Feral_Cat(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 5
    def __init__(self, x, y):
        fighter_class = Fighter_Class("feral cat", strength = 3, defense = 1, accuracy = 4, intelligence = 0, dexterity = 0, max_hp = 15)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 2)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "feral cat", "f", "orange", "A feral cat.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Gremlin(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 5
    def __init__(self, x, y):
        fighter_class = Fighter_Class("gremlin", strength = 6, defense = 3, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 20)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 4)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "gremlin", "d", "green", "A strange green gremlin", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Hobbit(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("hobbit", strength = 2, defense = 2, accuracy = 2, intelligence = 0, dexterity = 0, max_hp = 10)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 1)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "hobbit", "h", "green", "A short, weak humanoid.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Imp(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("imp", strength = 3, defense = 1, accuracy = 2, intelligence = 0, dexterity = 0, max_hp = 5)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 1)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "imp", "i", "red", "An extremely small and annoying demon.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Kobold(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("kobold", strength = 2, defense = 2, accuracy = 2, intelligence = 0, dexterity = 0, max_hp = 10)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 1)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "kobold", "k", "pink", "A weak pathetic being.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Nymph(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 5
    def __init__(self, x, y):
        fighter_class = Fighter_Class("nymph", strength = 5, defense = 3, accuracy = 5, intelligence = 0, dexterity = 0, max_hp = 30)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 4)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "nymph", "n", "blue", "An extremely dangerous creature.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Orc(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 10
    def __init__(self, x, y):
        fighter_class = Fighter_Class("orc", strength = 7, defense = 4, accuracy = 4, intelligence = 0, dexterity = 0, max_hp = 50)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 6)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "orc", "o", "red", "A large, strong orc.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Giant_Rat(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 3
    def __init__(self, x, y):
        fighter_class = Fighter_Class("giant rat", strength = 4, defense = 2, accuracy = 2, intelligence = 0, dexterity = 0, max_hp = 30)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 3)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "giant rat", "r", "grey", "A distgusting rat that is strangely large.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Cave_Spider(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 0
    def __init__(self, x, y):
        fighter_class = Fighter_Class("cave spider", strength = 2, defense = 1, accuracy = 1, intelligence = 0, dexterity = 0, max_hp = 5)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 1)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "cave spider", "s", "grey", "A common small spider.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Horse(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 4
    def __init__(self, x, y):
        fighter_class = Fighter_Class("horse", strength = 5, defense = 3, accuracy = 7, intelligence = 0, dexterity = 0, max_hp = 30)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 3)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "horse", "u", "grey", "A large warhorse.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Worm(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 2
    def __init__(self, x, y):
        fighter_class = Fighter_Class("worm", strength = 2, defense = 1, accuracy = 1, intelligence = 0, dexterity = 0, max_hp = 10)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 1)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "worm", "w", "pink", "A lorm squiggly worm.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Bat(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 12
    def __init__(self, x, y):
        fighter_class = Fighter_Class("bat", strength = 3, defense = 1, accuracy = 2, intelligence = 0, dexterity = 0, max_hp = 15)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 2)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "bat", "B", "red", "A large bat.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Centaur(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 15
    def __init__(self, x, y):
        fighter_class = Fighter_Class("centaur", strength = 7, defense = 4, accuracy = 5, intelligence = 0, dexterity = 0, max_hp = 30)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 5)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "centaur", "C", "cyan", "A half horse, half human creature.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Dragon(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 20
    def __init__(self, x, y):
        fighter_class = Fighter_Class("dragon", strength = 15, defense = 7, accuracy = 10, intelligence = 0, dexterity = 0, max_hp = 75)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 10)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "dragon", "D", "yellow", "An ancient dragon.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Gnome(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 9
    def __init__(self, x, y):
        fighter_class = Fighter_Class("gnome", strength = 5, defense = 3, accuracy = 4, intelligence = 0, dexterity = 0, max_hp = 40)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 4)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "gnome", "G", "brown", "A deceptively strong gnome.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Giant(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 18
    def __init__(self, x, y):
        fighter_class = Fighter_Class("giant", strength = 15, defense = 10, accuracy = 7, intelligence = 0, dexterity = 0, max_hp = 75)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 10)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "giant", "H", "yellow", "An extremely large, monsterous humanoid.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Lich(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 14
    def __init__(self, x, y):
        fighter_class = Fighter_Class("lich", strength = 10, defense = 5, accuracy = 5, intelligence = 0, dexterity = 0, max_hp = 50)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 7)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "lich", "L", "orange", "A magical lich.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Naga(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 13
    def __init__(self, x, y):
        fighter_class = Fighter_Class("naga", strength = 8, defense = 4, accuracy = 4, intelligence = 0, dexterity = 0, max_hp = 45)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 6)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "naga", "N", "red", "A monsterous being with the head of a human and the body of a snake.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Ogre(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 7
    def __init__(self, x, y):
        fighter_class = Fighter_Class("ogre", strength = 8, defense = 3, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 60)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 6)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "ogre", "O", "brown", "Strong humanoid monster.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Snake(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 3
    def __init__(self, x, y):
        fighter_class = Fighter_Class("snake", strength = 4, defense = 1, accuracy = 6, intelligence = 0, dexterity = 0, max_hp = 25)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 4)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "snake", "S", "green", "A slithering snake.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)

class Mob_Monkey(Entity):
    base_spawn_weight = 1
    lowest_level_spawn = 2
    def __init__(self, x, y):
        fighter_class = Fighter_Class("monkey", strength = 3, defense = 2, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 30)
        fighter_component = Fighter(fighter_class)
        level_component = Level(base_level = 1, base_xp = 50, lvl_up_factor = 3, xp_drop = 2)
        ai_component = Basic_Monster()
        equipment_component = Equipment()
        components_dict = {"ai": ai_component, "fighter": fighter_component, "level": level_component, "equipment": equipment_component}
        super().__init__(x, y, "monkey", "M", "grey", "A small and weak monkey.", blocks = True, render_order = Render_Order.ACTOR, components = components_dict)
