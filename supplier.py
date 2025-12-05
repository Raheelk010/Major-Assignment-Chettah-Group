# suppliers.py

suppliers = {}

def add_supplier():
    sup_id = input("Enter Supplier ID: ")
    name = input("Supplier Name: ")
    contact = input("Supplier Contact: ")

    suppliers[sup_id] = {"name": name, "contact": contact}
    print("Supplier added!\n")


def view_suppliers():
    print("\n---- Supplier List ----")
    for sid, info in suppliers.items():
        print(f"{sid} | {info['name']} | {info['contact']}")
    print()
