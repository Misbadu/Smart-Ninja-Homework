# coding: utf-8

# code created together with Andres

print "Welcome to Unit Converter. Here you can convert kilometers into miles."

while True:
    km = float(raw_input("Introduce the distance in kilometers (in number): "))
    miles = (km * 0.621)
    print "Number of miles: " + str(miles)

    question = raw_input("Do you want to make another conversion? Write yes or no: ")
    repeat = question.lower()

    if repeat == "no" or repeat == "n":
        print "Thank you. Have a nice day."
        break
    elif repeat == "yes" or repeat == "y":
        repeat = True
    else:
        print "This is not a valid input."
        break









