# main.py

from auth import login
from inventory import *
from sales import *
from customers import *
from suppliers import *
from reports import *

if login():

    while True:
        print("""
        ===== Pharmacy Management System =====
        1. Add Medicine
        2. View Inventory
        3. Update Stock
        4. Make Sale
        5. View Sales
        6. Customers
        7. Suppliers
        8. Inventory Report
        9. Sales Report
        0. Exit
        """)

        choice = input("Enter choice: ")

        match choice:
            case "1": add_medicine()
            case "2": view_inventory()
            case "3": update_stock()
            case "4": make_sale()
            case "5": view_sales()
            case "6": 
                add_customer()
                view_customers()
            case "7":
                add_supplier()
                view_suppliers()
            case "8": inventory_report()
            case "9": sales_report()
            case "0":
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid Choice!\n")
#