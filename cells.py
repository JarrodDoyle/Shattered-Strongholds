class Cell:
    """
    Base cell class inherited by all cell types
    """
    def __init__(self, cell_name, char, bk_color = "dark gray", color = "white", is_blocked = True, blocks_sight = True):
        self.cell_name = cell_name
        self.char = char
        self.bk_color = bk_color
        self.color = color
        self.is_blocked = is_blocked
        self.blocks_sight = blocks_sight
        self.explored = False

# ALL THE CELLS USED IN THE GAME
class Wall(Cell):
    def __init__(self):
        super().__init__("wall", "▒", is_blocked = True, blocks_sight = True)

class Floor(Cell):
    def __init__(self):
        super().__init__("floor", ".", is_blocked = False, blocks_sight = False)

class Rock(Cell):
    def __init__(self):
        super().__init__("rock", "#", is_blocked = True, blocks_sight = True)

class Stair_Down(Cell):
    def __init__(self):
        super().__init__("stair_down", ">", bk_color = "light blue", color = "light blue", is_blocked = False, blocks_sight = False)

class Stair_Up(Cell):
    def __init__(self):
        super().__init__("stair_up", "<", bk_color = "light blue", color = "light blue", is_blocked = False, blocks_sight = False)
