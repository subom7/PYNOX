# Problem Statement

When movie tickets are booked on paper or at a counter, mistakes are easy to make. The same seat can be given to two people, tickets get lost, and cancelling means going through notes to find one booking. If someone wants food at their seat, that is another queue. A small theatre needs something simple that keeps seats, tickets and snack orders in one place.

py-nox is a command-line movie ticket booking system written in Python. You pick a movie, see which seats are free, book a seat, view or cancel your ticket, and order snacks with a bill.

# Scope of the Project

What it does:
- Has a theatre layout with 3 sections (Recliners, Executive, Normal) and 9 seats in each row
- Books one seat at a time for the movie you choose
- Doesn't allow the same seat to be booked twice for the same movie
- Lets you view a ticket using the movie and your name
- Lets you cancel a ticket, after asking you to confirm
- Lets you order snacks from a menu file, with a bill that has 5% GST, and delivers to your seat
- Saves bookings in a text file for each movie, inside the bookings folder
- Keeps showing the menu until you choose Exit

# Target Users

- People who want to book, view or cancel a movie ticket and order snacks to their seat
- Students and beginners who want to see a simple Python project that uses functions, modules, loops, strings, lists and files
- Small theatre counters that need an easy way to keep track of seat bookings

# High-Level Features

1. Book Ticket: pick a movie, see the seat layout (☐ for free seats, ☒ for booked ones), enter a seat like A4, give your name and email, and get a ticket with a seat map marked 🗹
2. View Ticket: find your ticket using the movie and your name
3. Cancel Ticket: find your booking by name, see the seat and seat map, and confirm before it is removed
4. Order Snacks: read the menu from a text file, add items, get a bill with 5% GST, and confirm the order with your seat number or cancel it
5. Saved data: bookings are saved for each movie in bookings/movie-name.txt
6. Input checks: wrong seats, booked seats, empty names and bad emails are rejected and it asks again