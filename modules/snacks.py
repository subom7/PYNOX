import os
from modules.book_ticket import get_price


def load_menu():
    menu = []
    file = open("modules/menu/snacks_menu.txt", "r")
    for line in file:
        if line.strip() != "":
            menu.append(line.strip())
    file.close()
    return menu


def item_name(line):
    return line.split(" | ")[0]


def item_price(line):
    return int(line.split(" | ")[1])


def show_menu(menu):
    print("")
    print("--- SNACKS MENU (prices exclude GST) ---")
    for i in range(len(menu)):
        print(str(i + 1) + ". " + item_name(menu[i]) + " - Rs." + str(item_price(menu[i])))
    print(str(len(menu) + 1) + ". Exit")


def show_bill(ordered):
    total = 0
    print("")
    print("==================================")
    print("          SNACKS BILL")
    print("==================================")
    for line in ordered:
        print(item_name(line) + " : Rs." + str(item_price(line)))
        total = total + item_price(line)
    gst = total * 5 / 100
    print("----------------------------------")
    print("Subtotal : Rs." + "%.2f" % total)
    print("GST 5%   : Rs." + "%.2f" % gst)
    print("Total    : Rs." + "%.2f" % (total + gst))
    print("==================================")


def order_snacks():
    if not os.path.exists("modules/menu/snacks_menu.txt"):
        print("Menu file modules/menu/snacks_menu.txt not found.")
        return
    menu = load_menu()
    ordered = []
    exit_number = str(len(menu) + 1)
    show_menu(menu)
    billing = False
    while billing == False:
        if len(ordered) == 0:
            choice = input("Enter item number: ")
        else:
            choice = input("Enter next item number (" + exit_number + " to exit, Enter to start billing): ")
        if choice == exit_number:
            print("Order cancelled.")
            print("----------------------------------\n")
            return
        if choice == "" and len(ordered) > 0:
            billing = True
        elif choice.isdigit() and int(choice) >= 1 and int(choice) <= len(menu):
            item = menu[int(choice) - 1]
            ordered.append(item)
            print(item_name(item) + " added.")
        else:
            print("Invalid choice, try again.")

    show_bill(ordered)

    while True:
        seat = input("Enter your seat number to confirm order (or type cancel): ")
        seat = seat.upper()
        if seat == "CANCEL":
            print("Order cancelled.")
            print("----------------------------------\n")
            return
        if len(seat) == 2 and get_price(seat[0]) > 0 and seat[1] in "123456789":
            print("Order confirmed! Your snacks will be delivered to seat " + seat + ".")
            print("----------------------------------\n")
            return
        print("Invalid seat, try again.")