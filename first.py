import random

number = random.randint(1, 10)
tries = 1

print("I am thinking of a number betwen 1 & 10")
guess = int (input ("have a guess: "))
if guess > number:
    print("guess lower...")
if guess < number:
    print("guess higer...")
if guess == number:
    print("good job")
