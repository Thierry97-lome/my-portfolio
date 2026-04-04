import random

secret = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You got it! The number was {secret}.")
        print(f"It took you {attempts} attempts.")
        break

