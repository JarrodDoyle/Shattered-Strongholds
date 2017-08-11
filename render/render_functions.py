from bearlibterminal import terminal
import libtcodpy as libtcod
from fov_functions import *
from ui import *

def render(dungeon, player, entities, fov_map, fov_recompute, ui_elements):
    terminal.clear()
    recompute_fov(fov_recompute, fov_map, player)
    ui_elements["player"].render(player)
    ui_elements["monsters"].render(player, entities, fov_map)
    ui_elements["messages"].render()
    ui_elements["equipment"].render()
    ui_elements["description"].render()
    ui_elements["inventory"].render(player)
    ui_elements["dungeon"].render(player, entities, dungeon, fov_map)
    terminal.refresh()