# Awais Khan

from sales import sales_records
from inventory import inventory

def inventory_report():
    print("\n---- Inventory Report ----")
    for mid, info in inventory.items():
        print(f"{mid} - {info['name']} | Qty: {info['qty']} | Price: {info['price']}")
    print()


def sales_report():
    print("\n---- Sales Report ----")
    total_income = 0
    for sale in sales_records:
        total_income += sale["total"]
        print(f"Medicine: {sale['med_id']} | Qty: {sale['qty']} | Total: {sale['total']}")

    print(f"\nTotal Income: {total_income}\n")
