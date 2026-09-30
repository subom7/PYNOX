import os
from modules.book_ticket import show_movies, choose_movie, get_file_path, get_seat_map


def cancel_ticket():
    show_movies()
    movie = choose_movie()
    name = input("Enter your name: ")
    path = get_file_path(movie)
    found = False
    if os.path.exists(path):
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        new_lines = []
        for line in lines:
            data = line.split(" | ")
            if data[1].lower() == name.lower():
                found = True
                print("")
                print("Seat : " + data[0])
                print(get_seat_map(data[0]))
                print("==================================")
                answer = input("Cancel this ticket? (yes/no): ")
                if answer.lower() in ["yes","y"]:
                    print("Ticket for seat " + data[0] + " cancelled.")
                else:
                    print("Ticket not cancelled.")
                    new_lines.append(line)
            else:
                new_lines.append(line)
        file = open(path, "w")
        for line in new_lines:
            file.write(line)
        file.close()
    if found == False:
        print("No booking found for " + name + ".")