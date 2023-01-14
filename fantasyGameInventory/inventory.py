def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def displayInventory(inventory):
    print('Inventory:', end = "\n")
    item_total = 0
    for item in inventory:
        print(inventory[item], item, end = "\n")
        item_total += inventory[item]
    print('Total number of items: ' + str(item_total))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger' : 1, 'arrow' : 12}
addToInventory(stuff, ['rope', 'torch', 'poon', 'gold coin'])
displayInventory(stuff)