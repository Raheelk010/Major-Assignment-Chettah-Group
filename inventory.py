# Raheel khan

inventory = {}

def add_medicine():
    med_id = input("Enter Medicine ID: ")
    name = input("Enter Medicine Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    inventory[med_id] = {
        "name": name,
        "qty": qty,
        "price": price
    }

    print("Medicine added successfully!\n")


def view_inventory():
    print("\n---- Inventory List ----")
    for med_id, info in inventory.items():
        print(f"{med_id} | {info['name']} | Qty: {info['qty']} | Price: {info['price']}")
    print()


def update_stock():
    med_id = input("Enter Medicine ID to update: ")

    if med_id in inventory:
        add_qty = int(input("Enter new quantity to add: "))
        inventory[med_id]["qty"] += add_qty
        print("Stock updated!\n")
    else:
        print("Medicine not found!\n")
