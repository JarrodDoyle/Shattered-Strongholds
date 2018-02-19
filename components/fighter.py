from dice import roll_dice
from components.component_base import Component
import random

class Fighter(Component):
    # Fighter initialization
    def __init__(self, fighter_class):
        super().__init__()
        self.fighter_class = fighter_class
        self.hp = fighter_class.base_max_hp

    # Attack another fighter
    def attack(self, target):
        results = []

        attacker_accuracy = roll_dice(1, self.accuracy)
        target_defense = roll_dice(1, target.components["fighter"].defense)
        if attacker_accuracy > target_defense:
            weapon1 = self.owner.components.get("equipment").equipment.get("l_hand")
            if weapon1 == None:
                weapon1_damage = 0
            else:
                weapon1_damage = weapon1.damage

            weapon2 = self.owner.components.get("equipment").equipment.get("r_hand")
            if weapon2 == None:
                weapon2_damage = 0
            else:
                weapon2_damage = weapon2.damage

            # Damage is the diffence between the fighters strength and the enemy fighters defense
            damage = random.randint(self.strength // 2, self.strength) + weapon1_damage + weapon2_damage

            # Generate appropriate attack message and simulate attack
            results.append({"message": "[color={}]{}[color=red] dealt {} damage to [color={}]{}[color=red].".format(self.owner.color, self.owner.name.capitalize(), damage, target.color, target.name)})
            results.extend(target.components["fighter"].take_damage(damage))
        else:
            results.append({"message": "[color={}]{}'s[/color] attack missed".format(self.owner.color, self.owner.name.capitalize())})
        return results

    # Take damage
    def take_damage(self, damage):
        results = []

        # Take the damage
        self.hp -= damage

        # If fighter is dead return result saying so
        if self.hp <= 0:
            results.append({"dead": self.owner})
        return results

    # Calculates bonus strength from weapons and buffs and returns it
    def bonus_strength(self):
        return 0

    # Calculates bonus defense from armor and buffs and returns it
    def bonus_defense(self):
        return 0

    def bonus_accuracy(self):
        return 0

    # Calculates bonus intelligence from buffs and returns it
    def bonus_intelligence(self):
        return 0

    # Calculates bonus intelligence from buffs and returns it
    def bonus_dexterity(self):
        return 0

    @property
    def strength(self):
        return (self.fighter_class.base_strength + self.bonus_strength())

    @strength.setter
    def strength(self, value):
        self.fighter_class.base_strength = value

    @property
    def defense(self):
        return (self.fighter_class.base_defense + self.bonus_defense())

    @defense.setter
    def defense(self, defense):
        self.fighter_class.base_defense = defense

    @property
    def accuracy(self):
        return (self.fighter_class.base_accuracy + self.bonus_accuracy())

    @accuracy.setter
    def accuracy(self, accuracy):
        self.fighter_class.base_accuracy = accuracy

    @property
    def intelligence(self):
        return (self.fighter_class.base_intelligence + self.bonus_intelligence())

    @intelligence.setter
    def intelligence(self, intelligence):
        self.fighter_class.base_intelligence = intelligence

    @property
    def dexterity(self):
        return (self.fighter_class.base_dexterity + self.bonus_dexterity())

    @dexterity.setter
    def dexterity(self, value):
        self.fighter_class.base_dexterity = value

    @property
    def max_hp(self):
        return self.fighter_class.base_max_hp

    @max_hp.setter
    def max_hp(self, hp):
        self.fighter_class.base_max_hp = hp

class Fighter_Class:
    def __init__(self, name, strength, defense, accuracy, intelligence, dexterity, max_hp):
        self.class_name = name
        self.base_strength = strength
        self.base_defense = defense
        self.base_accuracy = accuracy
        self.base_intelligence = intelligence
        self.base_dexterity = dexterity
        self.base_max_hp = max_hp

class Barbarian(Fighter_Class):
    def __init__(self):
        super().__init__(name = "barbarian", strength = 4, defense = 1, accuracy = 3, intelligence = 0, dexterity = 0, max_hp = 100)
        self.description = "Barbarians are very strong and fairly accurate with their attacks. They have a lot of health which allows them to survive long, close range, fights. However they severely lack abilities with magic and ranged weapons."

class Wizard(Fighter_Class):
    def __init__(self):
        super().__init__(name = "wizard", strength = 2, defense = 1, accuracy = 2, intelligence = 5, dexterity = 0, max_hp = 50)
        self.description = "Wizards are extremely strong with magical attacks and are trained in some hand to hand combat. They lack ability with ranged weapons."

class Rogue(Fighter_Class):
    def __init__(self):
        super().__init__(name = "rogue", strength = 2, defense = 1, accuracy = 4, intelligence = 0, dexterity = 2, max_hp = 75)
        self.description = "Rogues are capable in all standard combat methods but struggle with magic attacks."

class Ranger(Fighter_Class):
    def __init__(self):
        super().__init__(name = "ranger", strength = 1, defense = 1, accuracy = 4, intelligence = 0, dexterity = 5, max_hp = 25)
        self.description = "Rangers are extremely good with ranged weapons and are accurate shots, they are however very weak and struggle in close combat situations."

class God(Fighter_Class):
    def __init__(self):
        super().__init__(name = "god", strength = 1000, defense = 1000, accuracy = 1000, intelligence = 1000, dexterity = 1000, max_hp = 1000)
        self.description = "You're a GOD with almost no weaknesses."
