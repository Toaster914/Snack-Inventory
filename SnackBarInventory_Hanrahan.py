'''
Snack Bar invintory
Toaster914
4/26/23
Python 2
'''

import os
file_name = "invintory.txt"

def main_menu():
    '''
    Handles the main menu.
    '''
    while True:
        if not os.path.exists(file_name):
            print("The", file_name, "file does not exist. Creating one now.")
            open(file_name, "x")

        print("1 - Add items")
        print("2 - Change item quantity")
        print("3 - View invintory")
        print("4 - Exit")

        selection = int(input("Enter your choice (1-4) >> "))
        if selection == 1:
            add_items()
        elif selection == 2:
            change_items()
        elif selection == 3:
            view_items()
        else:
            break

def add_items():
    '''
    Adds items to the file.
    '''
    file = open(file_name, "r")
    entries = file.readlines()
    file.close()

    full_split = []
    for i in range(0, len(entries)):
        feilds = entries[i].split(",")
        full_split += feilds

    repeat = "y"

    while repeat == "y":
        item_name = input("Enter the name of the item >> ").lower().strip()

        if item_name in full_split:
            print("That item already exists!")
            break

        price = input("Enter the price of the item >> ").lower().strip()
        amount = input("Enter the amount of items >> ").lower().strip()
        full_split.append(item_name)
        file = open(file_name, "a")
        file.write(item_name + "," + amount + "," + price + "\n")
        file.close()
        repeat = input("Would you like to add another item? (y/n) >> ").lower()
        print()

def change_items():
    '''
    Changes the quantity of an item in the file.
    '''
    file = open(file_name, "r")
    entries = file.readlines()
    file.close()

    loop = "y"
    while loop == "y":
        item_name = input("Enter the name of the item >> ").lower().strip()
        index = -1
        for i in range(0, len(entries)):
            feilds = entries[i].split(",")
            if feilds[0] == item_name:
                index = i
                price = feilds[2].strip()
                break
        if index == -1:
            print("That item is not in invintory.")
        else:
            new_quantity = input("Enter the new quantity for the item (negitive to delete) >> ")
            if int(new_quantity) < 0:
                entries.pop(index)
            else:
                entries[index] = item_name + "," + new_quantity + "," + price + "\n"
        loop = input("Would you like to change the quantity of another item? (y/n) >> ").lower()

    file = open(file_name, "w")
    file.writelines(entries)
    file.close()

def view_items():
    '''
    Veiws the items in the file.
    '''
    file = open(file_name, "r")
    enteries = file.readlines()
    file.close()

    for i in range(0, len(enteries)):
        print(feilds[0] + " - " + feilds[1], "at $" + feilds[2].strip())
    print()

main_menu()
