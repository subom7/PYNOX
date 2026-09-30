from modules.book_ticket import book_ticket
from modules.view_ticket import view_ticket
from modules.cancel_ticket import cancel_ticket
from modules.snacks import order_snacks

while True:
    print("")
    print("1. Book Ticket")
    print("2. View Ticket")
    print("3. Cancel Ticket")
    print("4. Order Snacks")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book_ticket()
    elif choice == "2":
        view_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        order_snacks()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice, try again.")