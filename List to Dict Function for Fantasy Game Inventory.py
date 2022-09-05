# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary
# representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like
# dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory.
# Note that the addedItems list can contain multiples of the same item.

from collections import Counter


# inventory parameter is a dictionary representing the player's inventory, addedItems is a list like dragonloot
def addToInventory(inventory, addedItems):
    x = dict(Counter(addedItems))
    total = Counter(inventory) + Counter(x)
    return total


# displayInventory that was created in the Fantasy Game Inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = sum(list(inventory.values()))
    print("Total number of items: " + str(item_total))


inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
addToInventory(inv, dragonLoot)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
