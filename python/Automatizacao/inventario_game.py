inventario = {"rope": 3, "circle": 3, "arrow": 5}

def display_inventory(inventory):
    total_items = 0
    print("Inventory: ")
    for key, value in inventory.items():
        print(f"{value} {key}")
        total_items += value

    print(f"Total items in inventory: {total_items}")

def add_to_inventory(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory.setdefault(item, 1)


display_inventory(inventario)
lista = ["arrow", 'gold coins', "eggs", "gold coins"]
add_to_inventory(inventario, lista)
display_inventory(inventario)