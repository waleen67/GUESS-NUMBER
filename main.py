import random

lowest_num = 1
highest_num = 100
guess_num = random.randint(lowest_num, highest_num)

attempts = 0
is_running = True

print("="*40)
print("Welcome to the Guess Game")
print(f"Please enter a number between {lowest_num} and {highest_num}")
print("="*40)

while is_running:
    guess = input("Guess a number between 1 and 100: ")

    if guess.isdigit():
        guess = int(guess)
        attempts += 1

        
        if guess > highest_num or guess < lowest_num:
            print("That number is out of range")
            print(f"Please enter a number between {lowest_num} and {highest_num}")

        elif guess > guess_num:
            print("That number is too high")

        elif guess < guess_num:
            print("That number is too low")

        else:
            print(f"Correct! The number is {guess}")
            print(f"Number of guesses: {attempts}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please enter a number between {lowest_num} and {highest_num}")
