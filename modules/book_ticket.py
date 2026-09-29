import os

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


def get_file_path(movie):
    name = movie.lower()
    name = name.replace(":", "")
    name = name.replace(" ", "-")
    return "bookings/" + name + ".txt"


def get_booked_seats(movie):
    booked = []
    path = get_file_path(movie)
    if os.path.exists(path):
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            if line.strip() != "":
                booked.append(line[0:2])
    return booked


def show_row(row, booked):
    line = row + "   "
    for col in range(1, 10):
        seat = row + str(col)
        if seat in booked:
            line = line + "☒ "
        else:
            line = line + "☐ "
        if col == 2 or col == 7:
            line = line + "  "
    print(line)


def show_theatre(booked):
    print("")
    print("    1 2   3 4 5 6 7   8 9")
    print("")
    print("      RECLINERS (Rs.349)")
    show_row("K", booked)
    show_row("J", booked)
    show_row("I", booked)
    print("")
    print("      EXECUTIVE (Rs.249)")
    show_row("H", booked)
    show_row("G", booked)
    show_row("F", booked)
    show_row("E", booked)
    show_row("D", booked)
    print("")
    print("      NORMAL (Rs.149)")
    show_row("C", booked)
    show_row("B", booked)
    show_row("A", booked)
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


def choose_seat(booked):
    while True:
        seat = input("Enter seat number (example: A4, D7, E4): ")
        seat = seat.upper()
        if len(seat) == 2 and get_price(seat[0]) > 0 and seat[1] in "123456789":
            if seat in booked:
                print("Seat " + seat + " is already booked. Please choose another seat.")
            else:
                return seat
        else:
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


def save_booking(movie, seat, name, email):
    if not os.path.exists("bookings"):
        os.mkdir("bookings")
    line = seat + " | " + name + " | " + email + " | Rs." + str(get_price(seat[0])) + "\n"
    file = open(get_file_path(movie), "a")
    file.write(line)
    file.close()


def book_ticket():
    show_movies()
    movie = choose_movie()
    print("You selected: " + movie)

    booked = get_booked_seats(movie)
    show_theatre(booked)
    seat = choose_seat(booked)

    name = get_name()
    email = get_email()

    save_booking(movie, seat, name, email)

    ticket = make_ticket(movie, seat, name, email)
    print("")
    print(ticket)
    print("Booking saved.")