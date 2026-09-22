VERSION = "1.0"


def greet_user(name):
    return f"Hello, {name}! Welcome to Git and GitHub."


def show_version():
    return f"Application version: {VERSION}"


name = input("Enter your name: ")

message = greet_user(name)

print(message)
print(show_version())
