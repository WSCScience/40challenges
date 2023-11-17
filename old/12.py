import random

rnum = random.randint(1, 11)

guess = int(input("Please guess the number between 1 and 10: "))

if guess == rnum:
    print("Correct")
else:
    print("Incorrect")