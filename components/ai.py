import libtcodpy as libtcod
import math
from entities.entity_functions import *
from components.component_base import Component

class Base_AI(Component):
    """
    Base AI class to be built off of.
    """
    def move(self, dx, dy):
        """
        Move the owning entity by passed offset.
        """
        self.owner.x += dx
        self.owner.y += dy

    def move_astar(self, target, entities, dungeon):
        """
        Move the owning entity using A*

        target -- target entity to move towards
        entities -- list of all entities on the dungeon floor
        dungeon -- dungeon object
        """
        owner = self.owner

        # Initialize FOV map for self
        fov = libtcod.map_new(dungeon.width, dungeon.height)

        # Set FOV map properties using the dungeon map
        for y in range(dungeon.height):
            for x in range(dungeon.width):
                # Set visible and walkable properties
                tile = dungeon.tiles[y][x]
                libtcod.map_set_properties(fov, x, y, not tile.blocks_sight, not tile.is_blocked)

        # Check for entities that need to be navigated around
        for entity in entities:
            if entity.blocks and entity != self and entity != target:
                # Set the tile at corresponding x and y as unwalkable
                libtcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Create a new A* path
        # Diagonal movement cost of sqrt 2, cost of 0.0 will prohibit diagonal movement
        path = libtcod.path_new_using_map(fov, 1.41)

        # Compute the path between self and target
        libtcod.path_compute(path, owner.x, owner.y, target.x, target.y)

        # If there is a possible path and it is shorter than 25 tiles
        # Short path size so monsters will not run all the way around map if path to player is blocked by another entity for example in a narrow corridor
        if not libtcod.path_is_empty(path) and libtcod.path_size(path) < 25:
            # Get coordinate of next location in the path
            x, y = libtcod.path_walk(path, True)
            if x or y:
                owner.x = x
                owner.y = y
        else:
            # Use a standard movement function and move towards player even if that path is blocked
            self.move_towards(target.x, target.y, dungeon, entities)

        # Delete path from memory
        libtcod.path_delete(path)

    def move_towards(self, target_x, target_y, dungeon, entities):
        """
        Move owning entity towards target x/y.

        target_x -- x value to move towards
        target_y -- y value to move towards
        dungeon -- dungeon object
        entities -- list of entities on dungeon floor
        """
        owner = self.owner
        dx = target_x - owner.x
        dy = target_y - owner.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Turns dx/dy into integers in range(-1, 1) inclusive
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        destination_x = owner.x + dx
        destination_y = owner.y + dy

        # If destination tile is not blocked and there are no blocking entities at destination
        entity = get_blocking_entity(entities, destination_x, destination_y)
        if not (dungeon.tiles[destination_y][destination_x].is_blocked or entity is not None):
            # Move self
            self.move(dx, dy)

class Basic_Monster(Base_AI):
    """
    Basic AI class used for monsters.
    """
    def take_turn(self, target, fov_map, dungeon, entities):
        """
        Take a turn.

        target -- entity to move towards (usually the player)
        fov_map -- Field of view map
        dungeon -- A dungeon object
        entities -- List of entities on the dungeon floor
        """
        results = []
        monster = self.owner

        # If monster is in players FOV
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            # If monster is not directly next to player
            if monster.distance_to(target) >= 2:
                # Move towards player using A* pathfinding
                self.move_astar(target, entities, dungeon)
            # Else attack player if they're alive
            elif target.components["fighter"].hp > 0:
                attack_results = monster.components["fighter"].attack(target, "hand")
                results.extend(attack_results)
        return results
