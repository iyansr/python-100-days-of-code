import random

print("Welcome to guessing number game")
print("I'm thinking number between 1 and 100")

secret_number = random.randint(1, 100)
is_game_over = False

attempts = 0
dificulty = input("Choose your dificulty, type 'easy' or 'hard' : ")

if dificulty == "easy":
    attempts = 10
elif dificulty == "hard":
    attempts = 5


def guessing():
    print(f"You have {attempts} attempts remaining to guess the number")
    guessed = int(input("Make a guess : "))
    return guessed


while not is_game_over:
    number = guessing()
    if number == secret_number:
        print(f"You're right, the number is {secret_number}")
        is_game_over = True
    elif number > secret_number:
        print("Too high")
        attempts -= 1
    elif number < secret_number:
        print("Too low")
        attempts -= 1
