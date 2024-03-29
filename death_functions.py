import libtcodpy as libtcod
from game_states import *
from render.render_classes import Render_Order

def kill_player(player):
    """
    Return the results of killing the player
    """
    player.char = "%"
    player.color = "dark red"
    message = "You died!"
    game_state = Game_States.PLAYER_DEAD
    return message, game_state

def kill_monster(monster):
    """
    Return the results of killing a monster
    """
    message = "[color={}]{}[/color] dies.".format(monster.color, monster.name.capitalize())
    monster.char = "%"
    monster.color = "dark red"
    monster.blocks = False
    monster.components.pop("fighter")
    monster.components.pop("ai")
    monster.description = "The decaying remains of {}.".format(monster.name)
    monster.name = "Remains of {}.".format(monster.name)
    monster.render_order = Render_Order.CORPSE
    return message
