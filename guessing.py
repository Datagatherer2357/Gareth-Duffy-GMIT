# Gareth Duffy 12-02-2018
# Guessing game
# Adapted from Stackoverflow

from random import randint

target = randint(1, 100) 
guess = 101

while guess != target:
    guess = int(input("guess a number between 1 and 100 please: "))
    if guess == target:
        print("congrats ! You guessed right!!")
    elif guess < target:
        print("too low bro")
    else:
        print("too high lad")