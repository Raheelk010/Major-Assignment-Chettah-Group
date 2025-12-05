# customers.py

customers = {}

def add_customer():
    cust_id = input("Enter Customer ID: ")
    name = input("Customer Name: ")
    contact = input("Customer Contact: ")

    customers[cust_id] = {"name": name, "contact": contact}
    print("Customer added successfully!\n")


def view_customers():
    print("\n---- Customer List ----")
    for cid, info in customers.items():
        print(f"{cid} | {info['name']} | {info['contact']}")
    print()
