from random import randint
import random
print ("The rules are: \n 1. If a player's guess is less than 1 or greater than 100, say OUT OF BOUNDS \n 2. On a player's first turn, if their guess is \n \t within 10 of the number, return WARM! \n \t further than 10 away from the number, return COLD! \n 3. On all subsequent turns, if a guess is \n \t closer to the number than the previous guess return WARMER! \n \t farther from the number than the previous guess, return COLDER! \n 4. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!")

while True:
    try:
        a = random.randint(1,100)
        Guess=int(input("Please enter the Guess  :"))
        if Guess == a:
             print ("CONGRATS The Guess is correct and it is", a)
        elif Guess > 100:
            print ("OUT OF BOUNDS and the Guess is" , a)
        elif Guess >= 1 and Guess <= 10:
            print("WARM and the Guess is", a)
        else:
            print("COLD and the Guess is", a)
    except ValueError:
        print("Invalid Input Please Enter the guess again and the guess is", a)
