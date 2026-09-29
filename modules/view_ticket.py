import os
from modules.book_ticket import show_movies, choose_movie, get_file_path, make_ticket


def view_ticket():
    show_movies()
    movie = choose_movie()
    path = get_file_path(movie)
    if not os.path.exists(path):
        print("No bookings found for this movie.")
        return
    name = input("Enter your name: ")
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    found = False
    for line in lines:
        if line.strip() != "":
            parts = line.strip().split(" | ")
            if parts[1].lower() == name.lower():
                print("")
                print(make_ticket(movie, parts[0], parts[1], parts[2]))
                found = True
    if not found:
        print("No ticket found for " + name + ".")