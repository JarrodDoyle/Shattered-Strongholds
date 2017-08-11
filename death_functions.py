import libtcodpy as libtcod
from game_states import *
from render.render_classes import Render_Order

def kill_player(player):
    player.char = "%"
    player.color = "dark red"
    message = "You died!"
    game_state = Game_States.PLAYER_DEAD
    return message, game_state

def kill_monster(monster):
    message = "[color={}]{}[/color] dies.".format(monster.color, monster.name.capitalize())
    monster.char = "%"
    monster.color = "dark red"
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = "remains of {}.".format(monster.name)
    monster.render_order = Render_Order.CORPSE
    return message