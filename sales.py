# sales.py

from inventory import inventory

sales_records = []

def make_sale():
    med_id = input("Enter Medicine ID: ")

    if med_id in inventory:
        qty = int(input("Enter Quantity: "))

        if qty <= inventory[med_id]["qty"]:
            total = qty * inventory[med_id]["price"]
            inventory[med_id]["qty"] -= qty

            sales_records.append({"med_id": med_id, "qty": qty, "total": total})

            print(f"Sale Successful! Total Bill = {total}\n")
        else:
            print("Not enough stock!\n")
    else:
        print("Medicine not found!\n")


def view_sales():
    print("\n---- Sales Records ----")
    for sale in sales_records:
        print(f"Medicine: {sale['med_id']} | Qty: {sale['qty']} | Total: {sale['total']}")
    print()
