import random

def number_game():
    number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

if __name__ == "__main__":
    number_game()