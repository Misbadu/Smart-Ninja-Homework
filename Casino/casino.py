# coding=utf-8
print "Welcome in the Casino"

guess = raw_input("Now enter the secret number: ")

secret = "25"

if guess == secret:
    print "Congratulations! You won this game!"
else:
    print "Not this time. Try again later."
