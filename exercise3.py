import random
number = random.rand.int(0,101)

while True:
    guess = int(input("Guess the number: "))
    if guess > number:
        print("Decrease your number: ")
    elif guess < number:
        print("Increase your number: ")
    else:
        print("You guessed correctly!")
