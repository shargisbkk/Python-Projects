import random

CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?><"

print("Hi! I'm Gen.")

while True:
    choice = ""
    listPass = []
    numPass = int(input("How many passwords do you need? Input: "))
    lengthPass = int(input("What length do they need to be? Input: "))

    for pwd in range(numPass):
        passwords = ""
        for char in range(lengthPass):
            passwords += random.choice(CHARACTERS)
        listPass.append(passwords)

    print(listPass)

    while choice != "y" and choice != "n":
        choice = input("would you like to make more passwords? (y/n): ").lower()
    if choice == "n":
        break

print("Good luck! (>.<)")