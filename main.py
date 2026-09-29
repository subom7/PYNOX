movies = [
    "Interstellar",
    "Odyssey",
    "Project Hail Mary",
    "End Game: Encore",
    "Dune: Three",
    "Ramayana",
    "La La Land",
    "Rockstar"
]


def show_movies():
    print("--- NOW SHOWING ---")
    for i in range(len(movies)):
        print(str(i + 1) + ". " + movies[i])


def get_price(row):
    if row in "KJI":
        return 349
    elif row in "HGFED":
        return 249
    elif row in "CBA":
        return 149
    else:
        return 0


def get_section(row):
    if row in "KJI":
        return "RECLINERS"
    elif row in "HGFED":
        return "EXECUTIVE"
    else:
        return "NORMAL"


def show_row(row):
    line = row + "   "
    for col in range(1, 10):
        line = line + "☐ "
        if col == 2 or col == 7:
            line = line + "  "
    print(line)


def show_theatre():
    print("")
    print("    1 2   3 4 5 6 7   8 9")
    print("")
    print("      RECLINERS (Rs.349)")
    show_row("K")
    show_row("J")
    show_row("I")
    print("")
    print("      EXECUTIVE (Rs.249)")
    show_row("H")
    show_row("G")
    show_row("F")
    show_row("E")
    show_row("D")
    print("")
    print("      NORMAL (Rs.149)")
    show_row("C")
    show_row("B")
    show_row("A")
    print("")
    print("      ------- SCREEN -------")
    print("")


def choose_movie():
    while True:
        choice = input("Enter movie number: ")
        if choice.isdigit():
            number = int(choice)
            if number >= 1 and number <= len(movies):
                return movies[number - 1]
        print("Invalid choice, try again.")


def choose_seat():
    while True:
        seat = input("Enter seat number (example: A4, D7, E4): ")
        seat = seat.upper()
        if len(seat) == 2 and get_price(seat[0]) > 0 and seat[1] in "123456789":
            return seat
        print("Invalid seat, try again.")


def get_name():
    name = input("Enter your name: ")
    while name == "":
        name = input("Name cannot be empty. Enter your name: ")
    return name


def get_email():
    email = input("Enter your email: ")
    while "@" not in email or "." not in email:
        email = input("Invalid email. Enter your email: ")
    return email


def make_ticket(movie, seat, name, email):
    ticket = "==================================\n"
    ticket = ticket + "         MOVIE TICKET\n"
    ticket = ticket + "==================================\n"
    ticket = ticket + "Movie : " + movie + "\n"
    ticket = ticket + "Name  : " + name + "\n"
    ticket = ticket + "Email : " + email + "\n"
    ticket = ticket + "Seat  : " + seat + " (" + get_section(seat[0]) + ")\n"
    ticket = ticket + "Price : Rs." + str(get_price(seat[0])) + "\n"
    ticket = ticket + "==================================\n"
    return ticket


show_movies()
movie = choose_movie()
print("You selected: " + movie)

show_theatre()
seat = choose_seat()

name = get_name()
email = get_email()

ticket = make_ticket(movie, seat, name, email)
print("")
print(ticket)