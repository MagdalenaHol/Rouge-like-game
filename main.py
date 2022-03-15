import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = '@'
    return player


def add_to_inventory(inventory: dict, added_items: list) -> dict:
    """Add to the inventory dictionary a list of items from added_items."""
    for key in added_items:
        if key not in inventory:
            inventory[key] = 1
        elif key in inventory:
            inventory[key] += 1
    return inventory
  

#print(add_to_inventory({'gold': 45, 'arrow': 12, 'torch': 6, 'rope': 2}, ['sword', 'sword', 'axe']))


def remove_from_inventory(inventory: dict, removed_items: list) -> dict:
    """Remove from the inventory dictionary a list of items from removed_items."""
    for key in removed_items:
        if key in inventory:
            inventory[key] -= 1
    inv_copy = inventory.copy()
    for item, count in inv_copy.items():
        if count <= 0:
            inventory.pop(item)
    return inventory


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        #engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        engine.movement_phase(board, player)
        util.clear_screen()


if __name__ == '__main__':
    main()
