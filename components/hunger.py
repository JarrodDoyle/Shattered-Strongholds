from components.component_base import Component
from game_states import Hunger_States

class Hunger(Component):
    def __init__(self, turns_to_starve, starve_damage = 1):
        self.turns_to_starve = turns_to_starve
        self.starve_damage = starve_damage
        self.turns = 0
        self.state = Hunger_States.FULL

    def update(self):
        results = []
        prev_state = self.state


        if self.state == Hunger_States.STARVING:
            results.extend(self.owner.components["fighter"].take_damage(self.starve_damage))

        if self.turns < self.turns_to_starve // 2:
            self.turns += 1
            self.state = Hunger_States.FULL
            message_state = "full"
        elif self.turns < self.turns_to_starve:
            self.turns += 1
            self.state = Hunger_States.HUNGRY
            message_state = "hungry"
        else:
            self.state = Hunger_States.STARVING
            message_state = "starving"

        if self.state != prev_state:
            results.append({"message": "[color=light red]You are now {}.[/color]".format(message_state)})
        return results