VALID_USERNAME = "admin"
VALID_PASSWORD = "secret123"


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("Login Successful!")
    else:
        print("Invalid username or password")


login()
