

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    dicc = dict()
    
    for key in set(items):
        dicc[key] = items.count(key)
            
    return dicc

inventario=print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    
    for key in set(items):
        if key in inventory:
            inventory[key] = inventory[key] + 1
        else:
            inventory[key] = 1
    return inventory
        
    

inventory2 = add_items({"coal":1}, ["wood", "iron", "coal", "wood"])


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    
    """
    for key in set(items):
        if items.count(key) <= inventory[key]:
            inventory[key] -= items.count(key)
        else: 
            inventory[key] = 0           
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    lists = []
    for item in inventory.items():
        if item[1] > 0:
            lists+= [item]
    return lists
