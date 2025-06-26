items = ['skis', 'snowboard', 'goggles', 'boots']
inventory = [10, 0, 0, 7]

# create a dictionary with item names as keys, 'sold out' if inventory == 0, or value if inventory != 0

inventory_status = {}

for i, item in enumerate(items):
    if inventory[i] == 0:
        inventory_status[item] = 'sold out'
    else:
        inventory_status[item] = inventory[i]

inventory_status