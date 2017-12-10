# coding: utf-8

"""Homework 9.2: Restaurant menu
A nearby restaurant owner'd like to have a program where he'd enter their daily menu and it would get saved into a menu.txt file.
The menu would consist of a dish (like "Beef steak with potatoes" and a price of the dish (e.g. 5.40).
When you finish, push your code on GitHub and share it on the SmartNinja forum."""

print "Restaurant Menu"

my_menu = {}

while True:
    dish = raw_input("Add a dish: ")
    dish_price = float(raw_input("Add a price: "))
    new_dish = raw_input("Would you like to add another dish? (yes/no): ").lower()
    if new_dish == "yes" or new_dish == "y":
        my_menu[dish] = dish_price
    else:
        my_menu[dish] = dish_price
        break

with open ("menu.txt", "w+") as menu_file:

    print "Restaurant Menu for today: "
    menu_file.write("Restaurant Menu for today:  \n" + "\n")
    for dish in my_menu:
        print str(dish) + " " + str(my_menu[dish]) + " Euro"
        menu_file.write(str(dish) + " " + str(my_menu[dish]) + " Euro" + "\n")
    print "END"
