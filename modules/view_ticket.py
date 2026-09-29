import os
from modules.book_ticket import show_movies, choose_movie, get_file_path, make_ticket


def view_ticket():
    show_movies()
    movie = choose_movie()
    name = input("Enter your name: ")
    path = get_file_path(movie)
    found = False
    if os.path.exists(path):
        file = open(path, "r")
        for line in file:
            data = line.split(" | ")
            if data[1].lower() == name.lower():
                print("")
                print(make_ticket(movie, data[0], data[1], data[2]))
                found = True
        file.close()
    if found == False:
        print("No ticket found for " + name + ".")