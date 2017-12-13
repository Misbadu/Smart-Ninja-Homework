# coding=utf-8
import random

print "Welcome in the Casino"

secret_num = random.randint(0, 19)
while True:
    guess = int(raw_input("Enter the secret number (between 1 and 20): "))
    if guess > secret_num:
        print "The number is smaller than your guess. Try again."
    elif guess < secret_num:
        print "The number is bigger than your guess. Try again."
    else:
        print "Congratulations! You won this game!"
        break

