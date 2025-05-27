import random
import os
import sys


def secret_number():
    """Generates a random 4-digit secret number."""
    
    return str(random.randint(1000, 9999))


def user_guess():
    """Prompts the user to enter a 4-digit guess.""" 
    
    separator = '-' * 40
    return str(input(f"Enter a 4-digit number: \n{separator}\n>>> "))


def calculate_bulls(secret_number, guess):
    """Calculates the number of bulls for user's guess."""
    
    bulls = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
    return bulls


def calculate_cows(secret_number, guess):
    """Calculates the number of cows for user's guess."""
    
    cows = 0
    secret_digits = list(secret_number)
    guessed_digits = list(guess)
    for i in range(4):
        if guess[i] == secret_number[i]:
            secret_digits.remove(guess[i])
            guessed_digits.remove(guess[i])
    for j in guessed_digits:
        if j in secret_digits:
            cows += 1
            secret_digits.remove(j)
    return cows


def print_results(bulls, cows):
    """Prints the results of user's guess."""
    
    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bulls_text}, {cows} {cows_text}")
    

def print_winning_message(attempts):
    """Prints a congratulatory message when the user wins."""
    
    separator = '-' * 40
    attempts_text = "attempt" if attempts == 1 else "attempts"
    print(f"Congratulations! You guessed the right number in", 
        f"{attempts} {attempts_text}!")
    print(separator)
    

def play_again():
    """Asks the user if they want to play again and
    either restarts the game or ends it."""
    
    while True:
        replay = input("Play again: (y/n)? ").lower()
        if replay == 'y':
            os.system('cls')
            all_game()
            break
        elif replay == 'n':
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Invalid input. Please type only 'y' or 'n'.")

def all_game():
    """Main game loop that runs the Bulls and Cows game."""
    
    separator = '-' * 40
    game_on = True
    number = secret_number()    
    attempts = 0
    
    while game_on:
        guessing = user_guess()
        if guessing.lower() == "q":
            print('quitting the game')
            sys.exit()
        elif len(guessing) != 4 or not guessing.isdigit():
            os.system('cls')
            print("Invalid input. Please enter a 4-digit number", 
                  "(or press 'q' to quit).")
            continue
        attempts += 1

        print(separator)
        bulls = calculate_bulls(number, guessing)
        cows = calculate_cows(number, guessing)

        nr_bulls = bulls
        nr_cows = cows

        print_results(nr_bulls, nr_cows)

        if nr_bulls == 4:
            print_winning_message(attempts)
            play_again()
            break

if __name__ == "__main__":
    all_game()