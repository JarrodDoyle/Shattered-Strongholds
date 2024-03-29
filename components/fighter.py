from dice import roll_dice
from components.component_base import Component
import random

class Fighter(Component):
    """
    Fighter component inheriting from Component.

    Controls attacking, taking damage, and the associated stats.
    """
    def __init__(self, fighter_class):
        """
        Initialize fighter component.

        fighter_class -- The name of the fighters class (e.g. barbarian)
        """
        super().__init__()
        self.fighter_class = fighter_class
        self.hp = fighter_class.base_max_hp

    def attack(self, target, slot):
        """
        Return the results of an attack attempt on a target.

        target -- The entity to be attacked
        slot -- The weapon slot to use in the attack
        """
        results = []
        weapon_damage = []

        # If alive
        if self.hp > 0:
            # Do a dice roll for self accuracy and targets defense.
            attacker_accuracy = roll_dice(1, self.accuracy)
            target_defense = roll_dice(1, target.components["fighter"].defense)
            if attacker_accuracy > target_defense:
                # Get the weapon held at the specified equipment slot.
                weapon = self.owner.components.get("equipment").equipment.get(slot)

                if weapon == None:
                    # If fighter doesn't have a weapon in the specified slot, deal a random amount of damage in the specified range
                    weapon_damage.append(random.randint(max(self.strength // 2, 1), self.strength))
                else:
                    # Else call the weapon's damage function and extend the damage list with the results of the call
                    weapon_damage.extend(weapon.components["weapon"].damage(self))

                # Total up all of the damage dealt
                damage = 0
                for i in weapon_damage:
                    damage += i

                if damage > 0:
                    # Generate appropriate attack message and simulate attack
                    results.append({"message": "[color={}]{}[color=red] dealt {} damage to [color={}]{}[color=red].".format(self.owner.color, self.owner.name.capitalize(), damage, target.color, target.name)})
                    results.extend(target.components["fighter"].take_damage(damage))
                else:
                    results.append({"message": "[color={}]{}'s[/color] attack was unsuccesful.".format(self.owner.color, self.owner.name.capitalize())})
            else:
                results.append({"message": "[color={}]{}'s[/color] attack missed".format(self.owner.color, self.owner.name.capitalize())})
        return results

    # Take damage
    def take_damage(self, damage):
        """
        Reduce fighter HP and return the results.

        damage -- How much damage to be taken
        """
        results = []

        # Take the damage
        self.hp -= damage

        # If fighter is dead return result saying so
        if self.hp <= 0:
            self.hp == 0
            results.append({"dead": self.owner})
        return results

    # Returns the amount of a specified stat provided by the fighter's equipment
    def bonus_stat(self, stat):
        """
        Returns how much of a stat is given as bonuses by equipment.

        stat -- The name of the stat to be returned
        """
        equipment_component = self.owner.components.get("equipment")
        stat_sum = 0
        # If the fighter has an equipment component
        if equipment_component:
            # For each equipment slot
            for item in equipment_component.equipment.items():
                if item[1] is not None and item[0] != "arrows":
                    # Add stat from weapon or armor respectively
                    if item[1].components.get("weapon"):
                        stat_sum += item[1].components["weapon"].get_stat(stat)
                    elif item[1].components.get("armor"):
                        stat_sum += item[1].components["armor"].get_stat(stat)
        return stat_sum

    @property
    def strength(self):
        return (self.fighter_class.base_strength + self.bonus_stat("strength"))

    @strength.setter
    def strength(self, value):
        self.fighter_class.base_strength = value

    @property
    def defense(self):
        return (self.fighter_class.base_defense + self.bonus_stat("defense"))

    @defense.setter
    def defense(self, defense):
        self.fighter_class.base_defense = defense

    @property
    def accuracy(self):
        return (self.fighter_class.base_accuracy + self.bonus_stat("accuracy"))

    @accuracy.setter
    def accuracy(self, accuracy):
        self.fighter_class.base_accuracy = accuracy

    @property
    def intelligence(self):
        return (self.fighter_class.base_intelligence + self.bonus_stat("intelligence"))

    @intelligence.setter
    def intelligence(self, intelligence):
        self.fighter_class.base_intelligence = intelligence

    @property
    def dexterity(self):
        return (self.fighter_class.base_dexterity + self.bonus_stat("dexterity"))

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
    """
    Base class inherited by different fighter "classes"
    """
    def __init__(self, name, strength, defense, accuracy, intelligence, dexterity, max_hp):
        """
        Initialize "fighter class"
        """
        self.class_name = name
        self.base_strength = strength
        self.base_defense = defense
        self.base_accuracy = accuracy
        self.base_intelligence = intelligence
        self.base_dexterity = dexterity
        self.base_max_hp = max_hp

# The four classes the player can choose from.
class Barbarian(Fighter_Class):
    description = "Barbarians are very strong and fairly accurate with their attacks. They have a lot of health which allows them to survive long, close range, fights. However they severely lack abilities with magic and ranged weapons.\n STR: 4\n DEF: 1\n ACC: 3\n INT: 1\n DEX: 5\n HP: 100"
    def __init__(self):
        super().__init__(name = "barbarian", strength = 4, defense = 1, accuracy = 3, intelligence = 1, dexterity = 1, max_hp = 100)

class Wizard(Fighter_Class):
    description = "Wizards are extremely strong with magical attacks and are trained in some hand to hand combat. They lack ability with ranged weapons.\n STR: 2\n DEF: 1\n ACC: 2\n INT: 5\n DEX: 1\n HP: 50"
    def __init__(self):
        super().__init__(name = "wizard", strength = 2, defense = 1, accuracy = 2, intelligence = 5, dexterity = 1, max_hp = 50)

class Rogue(Fighter_Class):
    description = "Rogues are capable in all standard combat methods but struggle with magic attacks.\n STR: 2\n DEF: 1\n ACC: 4\n INT: 1\n DEX: 2\n HP: 75"
    def __init__(self):
        super().__init__(name = "rogue", strength = 2, defense = 1, accuracy = 4, intelligence = 1, dexterity = 2, max_hp = 75)

class Ranger(Fighter_Class):
    description = "Rangers are extremely good with ranged weapons and are accurate shots, they are however very weak and struggle in close combat situations.\n STR: 1\n DEF: 1\n ACC: 4\n INT: 1\n DEX: 5\n HP: 25"
    def __init__(self):
        super().__init__(name = "ranger", strength = 1, defense = 1, accuracy = 4, intelligence = 1, dexterity = 5, max_hp = 25)
