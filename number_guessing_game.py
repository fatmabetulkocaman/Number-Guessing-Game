import random
import time

print(
    """

***************************
NUMBER PREDICTION GAME
------------------
Rules of the Game:
1.estimation range 1-75
2.Press '0' to exit the game.

***************************

"""
)


random_ = random.randint(1,75)

counter = 0

while True:

    counter += 1
    number = int(input("Enter your guess:"))

    if number == 0:
        print("Exiting the game...")
        time.sleep(4)
        print("Exited the game!")
        break

    elif number < random_:
        print("Being checking...")
        time.sleep(2.5)
        print("Enter a larger number!")
        continue

    elif number > random_:
        print("Being checking...")
        time.sleep(2.5)
        print("Enter a smaller number!")
        continue

    elif number == random_:
        print("Being checking...")
        time.sleep(2.5)
        print("Congratulations,your guess is correct!!")
        print("Randomly selected number: {}".format(random_))
        print("Number of guesses: {}".format(counter))
        time.sleep(2.5)
        print("Exiting the game...")
        time.sleep(4)
        print("Exited the game!")
        break

    else:
        print("Incorrect data entry!!!")
        continue
