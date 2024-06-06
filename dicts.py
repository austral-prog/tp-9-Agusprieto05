def create_inventory(my_list):
    my_dict = dict()
    for i in range(0, len(my_list)):
        if my_list[i] in my_dict.keys():
            my_dict[my_list[i]] += 1
        else:
            my_dict[my_list[i]] = 1
    return my_dict


def add_items(inventory, items):

    for i in range(0, len(items)):
        if items[i] not in inventory:
            inventory[items[i]] = 1
        else:
            inventory[items[i]] += 1
    return inventory

def decrement_items(inventory, items):
    for i in range(0, len(items)):
        if items[i] in inventory:
            inventory[items[i]] = inventory[items[i]] - 1
        if inventory[items[i]] <= 0:
            inventory[items[i]] = 0
    return inventory

def remove_item(inventory, item):
    for i in range(0, len(inventory)):
        if item in inventory:
            del inventory[item]
    return inventory

def list_inventory(inventory):
    mylist = []
    for i, value in inventory.items():
        if value > 0:
            mylist.append((i, value))
    return mylist
    lists = []
    for item in inventory.items():
        if item[1] > 0:
            lists+= [item]
    return lists
