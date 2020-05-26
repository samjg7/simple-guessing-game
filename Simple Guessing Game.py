import random

guess_count = 0
guess_limit = 3
secret_number = random.randint(1, 10)


guess = 0

while guess_count < guess_limit and guess != secret_number:
    guess = int(input("Guess the lucky number between 1 and 10: "))
    guess_count += 1
    if guess_count < 3 and guess_count != 2 and guess != secret_number:
        print(f"Try again! You have {guess_limit - guess_count} tries left.")
    elif guess_count < 3 and guess_count == 2 and guess != secret_number:
        print(f"Try again! You have {guess_limit - guess_count} try left.")
    elif guess_count > 2 and guess != secret_number:
        print(f"You lose! The correct answer was {secret_number}!")
    if guess == secret_number:
        print("You guessed the correct number!")
        break
