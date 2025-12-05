# auth.py

def login():
    print("---- Pharmacy System Login ----")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "123":
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Credentials!\n")
        return False
