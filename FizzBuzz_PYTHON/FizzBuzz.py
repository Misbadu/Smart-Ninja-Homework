# coding: utf-8

print "Welcome to FizzBuzz."
try:
    number = int(raw_input("If you want to play, enter a number from 1 to 100: "))
    print "Your number is: " + str(number)

    for number in range(1, number+1):
        if number % 3 == 0 and number % 5 == 0:
            print "fizzbuzz"
        elif number % 5 == 0:
            print "buzz"
        elif number % 3 == 0:
            print "fizz"
        else:
            print str(number)
except Exception as e:
    print "This is not a correct value."
print "Thank you."
