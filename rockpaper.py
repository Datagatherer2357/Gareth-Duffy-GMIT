import random
import time
# Introduction
print("""-----------WELCOME TO THE ROCK PAPER SCISSORS GAME-----------
FOR ROCK PRESS 0
FOR PAPER PRESS 1
FOR SCISSORS PRESS 2""")

# It takes the input from the user and assigns a value to user_move variable.
while True:
    print("TO QUIT THE GAME PRESS 3")
    user_move = ""
    usr_input = int(input())
    if usr_input == 0:
        user_move = "ROCK"
    if usr_input == 1:
        user_move = "PAPER"
    if usr_input == 2:
        user_move = "SCISSORS"
    if usr_input == 3:
        break
    if usr_input > 3:
        print("PLEASE ENTER A VALID MOVE.")
        continue
    print("USER :" + user_move)

