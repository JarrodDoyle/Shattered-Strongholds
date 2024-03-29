import random, targetting
from map_generation.bsp_map import Dungeon_BSP
from map_generation.cellular_automata import Dungeon_Cellular_Automata
from fov_functions import *
from render.render_functions import render
from input.input_functions import *
from ui import *
from game_states import Game_States
from entities.mobs import Player
from death_functions import kill_player, kill_monster
from entities.entity_functions import get_blocking_entity
from initialize import initialize_dungeon, initialize_player

class Game:
    """
    Game class containing main game loop
    """
    def __init__(self):
        """
        Initialize game
        """
        # Set inital game state
        self.game_state = Game_States.PLAYER_TURN
        self.previous_game_state = self.game_state

        # Initialize UI elements and dummy player object
        self.ui_elements = initialize_ui_elements()
        self.player = initialize_player()

        # Initialize first dungeon floor
        self.floor_index = 0
        self.dungeon, self.entities = initialize_dungeon(self.player, self.floor_index)
        self.floors = [[self.dungeon, self.entities]]

        # Initialize FOV
        self.init_fov()

        self.item = None

    def init_fov(self):
        """
        Initialize the FOV variables used in the game
        """
        self.fov_map, self.fov_recompute = initialize_fov(self.dungeon)
        self.fog_of_war = True

    def play(self):
        """
        Main game loop. Return the result of the "turn"
        """
        result = {}
        turn_results = []

        # Render UI and dungeon
        render(self.dungeon, self.player, self.entities, self.fov_map, self.fov_recompute, self.ui_elements, self.fog_of_war)

        # Get player action as a dict
        player_action = handle_inputs(self.game_state)
        move = player_action.get("move")
        rest = player_action.get("rest")
        pickup = player_action.get("pickup")
        inventory_active = player_action.get("inventory_active")
        inventory_index = player_action.get("inventory_index")
        cancel = player_action.get("cancel")
        quit = player_action.get("quit")

        # If player action is to quit then break the main loop
        if quit:
            result["quit"] = True

        # If the player is dead
        if self.game_state == Game_States.PLAYER_DEAD:
            if cancel:
                result["cancel"] = True

        # If it is the players turn
        if self.game_state == Game_States.PLAYER_TURN:
            if cancel:
                result["cancel"] = True

            # List to store all dicts of turn results
            player_turn_results = []

            if player_action.get("target"): # If player using a targetted attack
                weapon = self.player.components["equipment"].equipment["offhand"]
                # Set appropriate attack range depending on if the player has a
                # ranged weapon.
                if weapon is not None:
                    target_range = weapon.components["weapon"].attack_range
                else:
                    target_range = 1

                # If a target is chosen otherwise cancel or quit
                targetting_result = targetting.choose_target(self.player, self.entities, target_range, entity_type = "fighter")
                if targetting_result.get("target"):
                    # Attack target and change game state
                    target = targetting_result.get("target")
                    player_turn_results.extend(self.player.components["fighter"].attack(target, "offhand"))
                    self.game_state = Game_States.ENEMY_TURN
                elif targetting_result.get("cancel"):
                    pass
                elif targetting_result.get("quit"):
                    result["quit"] = True
                    return result

            # If the player wants to move
            if move:
                dx, dy = move
                destination_x = self.player.x + dx
                destination_y = self.player.y + dy
                # If the destination tile is walkable
                if not self.dungeon.tiles[destination_y][destination_x].is_blocked:
                    # Check if there are any blocking entities at destination
                    target = get_blocking_entity(self.entities, destination_x, destination_y)

                    # If there is a blocking entity at destination attack it
                    if target:
                        attack_results = self.player.components["fighter"].attack(target, "hand")
                        player_turn_results.extend(attack_results)
                    # Otherwise move to destination
                    else:
                        self.player.move(dx, dy)
                        self.fov_recompute = True
                    # Player turn is over so set game_state to ENEMY_TURN
                    self.game_state = Game_States.ENEMY_TURN

            # If player has chosen to do nothing
            if rest:
                # Player turn is over so set game_state to ENEMY_TURN
                self.game_state = Game_States.ENEMY_TURN

            # If player tries to pick something up
            if pickup:
                for entity in self.entities:
                    if entity.components.get("item") and entity.x == self.player.x and entity.y == self.player.y:
                        pickup_results = self.player.components["inventory"].add_item(entity)
                        break
                else:
                    pickup_results = [{"message": "[color=yellow]There is nothing here to pick up."}]
                player_turn_results.extend(pickup_results)

            # Player uses the stairs to go up/down
            if player_action.get("stair_used"):
                if self.dungeon.tiles[self.player.y][self.player.x].cell_name == "stair_down":
                    self.floor_index += 1
                    # If player on 26th floor they win
                    if self.floor_index == 25:
                        self.game_state = Game_States.WIN
                    # If floor hasn#t previously been visited generate a new one and add it to the floors list
                    elif self.floor_index >= len(self.floors):
                        self.dungeon, self.entities = initialize_dungeon(self.player, self.floor_index)
                        self.floors.append([self.dungeon, self.entities])
                    # Otherwise load dungeon and entities from floors list and update player coordinates/offset
                    else:
                        self.dungeon, self.entities = self.floors[self.floor_index]
                        self.player.x, self.player.y = self.dungeon.entrance
                        self.dungeon.set_player_offset(self.player)
                    player_turn_results.append({"message": "{} progresses deeper into the dungeon.".format(self.player.name)})
                elif self.dungeon.tiles[self.player.y][self.player.x].cell_name == "stair_up":
                    # Load previous dungeon and entities from floors list and update player coordinates/offset
                    if self.floor_index > 0:
                        self.floor_index -= 1
                        self.dungeon, self.entities = self.floors[self.floor_index]
                        self.player.x, self.player.y = self.dungeon.exit
                        self.dungeon.set_player_offset(self.player)
                        player_turn_results.append({"message": "{} ascends the stairs.".format(self.player.name)})
                    else:
                        player_turn_results.append({"message": "You cannot leave the dungeons."})
                self.fov_map, self.fov_recompute = initialize_fov(self.dungeon)

            # If player accesses inventory
            if inventory_active:
                self.previous_game_state = self.game_state
                self.game_state = Game_States.INVENTORY_ACTIVE
                player_turn_results.append({"message": "You open your inventory."})

            player_turn_results.extend(self.player.components["hunger"].update())

            turn_results.extend(player_turn_results)

        # If player is using the inventory
        if self.game_state == Game_States.INVENTORY_ACTIVE:
            results = []
            if inventory_index is not None:
                if inventory_index < len(self.player.components["inventory"].items):
                    index = -1
                    for items in self.player.components["inventory"].items.items():
                        if index == inventory_index:
                            self.item = items[1][0]
                        index += 1
                    if self.item is not None:
                        results.append({"message": "You look at the {}.".format(self.item.name)})
                        description = "{}\n Us(e)\n (d)rop\n E(x)amine".format(self.item.name)
                        self.ui_elements["description"].text = description
                        self.game_state = Game_States.USING_ITEM
            elif cancel:
                results.append({"message": "You close your inventory."})
                self.game_state = self.previous_game_state
            turn_results.extend(results)

        # If player looking at an item in inventory
        if self.game_state == Game_States.USING_ITEM:
            results =[]
            description = "{}\n Us(e)\n (d)rop\n E(x)amine".format(self.item.name)
            self.ui_elements["description"].text = description

            use = player_action.get("use")
            drop = player_action.get("drop")
            examine = player_action.get("examine")

            if use:
                # Use the item
                results.extend(self.item.components["item"].use(self.player, self.player.components["inventory"]))
                self.item = None
                self.game_state = Game_States.INVENTORY_ACTIVE
            if drop:
                # Drop the item
                results.extend(self.item.components["item"].drop(self.entities, self.player, self.player.components["inventory"]))
                self.item = None
                self.game_state = Game_States.INVENTORY_ACTIVE
            if examine:
                # Examine the item
                self.ui_elements["description"].text = self.item.description
                results.append({"message": "You decide to look more closely at the {}.".format(self.item.name)})
            if cancel:
                self.game_state = Game_States.INVENTORY_ACTIVE
            turn_results.extend(results)

        # If it is not the players turn
        if self.game_state == Game_States.ENEMY_TURN:
            results = []
            # For each entity that has an AI and is not the player
            for entity in self.entities:
                if entity != self.player and entity.x == self.player.x and entity.y == self.player.y:
                    self.ui_elements["description"].text = entity.description
                if entity.components.get("ai") and entity != self.player:
                    # Simulate entity turn and get results
                    results.extend(entity.components["ai"].take_turn(self.player, self.fov_map, self.dungeon, self.entities))
            # If the player does not die as a result of an entities turn set game_state to PLAYER_TURN
            else:
                self.game_state = Game_States.PLAYER_TURN
            turn_results.extend(results)

        if self.game_state == Game_States.WIN:
            # Display "You win" window
            win_screen = Generic_Text_Window(17, 1, 46, 46, "Congratulations!")
            win_screen.render("Congratulations you won! Review your inventory and character stats then press any key to go back to the main menu.")
            terminal.refresh()
            key = terminal.read()
            if key == terminal.TK_CLOSE:
                result["quit"] = True
            else:
                result["cancel"] = True


        for turn_result in turn_results:
            message = turn_result.get("message")
            dead_entity = turn_result.get("dead")
            item_added = turn_result.get("item_added")

            messages = []
            # If the players turn has generated a message add them to the messages list
            if message:
                self.ui_elements["messages"].messages.append(message)

            # If the players turn has resulted in an entity dying
            if dead_entity:
                # If the player has died generate an appropriate message and change game_state
                if dead_entity == self.player:
                    message, self.game_state = kill_player(dead_entity)
                    turn_results.append({"message": message})
                # Otherwise generate an appropriate message for the entities death
                else:
                    turn_results.append({"message": kill_monster(dead_entity)})
                    xp = dead_entity.components["level"].drop_xp()
                    turn_results.extend(self.player.components["level"].gain_xp(xp))

            # If the player picked up an item
            if item_added:
                # Remove item from entities list and therefore the dungeon map. Change game state to enemy turn
                self.entities.remove(item_added)
                self.game_state = Game_States.ENEMY_TURN

        return result
