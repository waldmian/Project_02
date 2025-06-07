"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Anna Waldhansová
email: annaw@email.cz
"""

import random
import os
import sys


def print_initial_greeting() -> None:
    """Prints initial greeting."""
    
    separator = '-' * 47
    print("Hi and welcome to the Bulls and Cows Game!")
    print(separator)
    print("I've generated a random 4-digit number for you.\nLet's play!")
    print(separator)


def secret_number() -> str:
    """Generates a random 4-digit secret number with unique digits.
    The first digit is not zero."""
    
    digits = [str(d) for d in range(10)]
    first_digit = random.choice(digits[1:])
    remaining_digits = random.sample([d for d in digits if d != first_digit], 3)
    return first_digit + ''.join(remaining_digits)


def user_guess() -> str:
    """Prompts the user to enter a valid 4-digit guess. 
    The guess must not start with 0 and must only contain unique digits.
    If the user enters 'q', the game will quit.
    """
    
    separator = '-' * 47
    while True:
        guess = input(f"Enter a 4-digit number: \n{separator}\n>>> ")
        if guess.lower() == "q":
            return guess
        if (
            len(guess) != 4
            or not guess.isdigit()
            or guess[0] == '0'
            or len(set(guess)) != 4
        ):
            print("Invalid input.",
                "\nPlease enter a 4-digit number with unique digits,",
                "that does not start with 0.", 
                "\n(Or enter 'q' to quit).")
            continue
    return guess


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


def clear_screen() -> None:
    """Clears the console screen on both Windows 
    and Unix-like systems."""
    
    os.system('cls' if os.name == 'nt' else 'clear')

def print_winning_message(attempts):
    """Prints a congratulatory message when the user wins."""
    
    separator = '-' * 47
    attempts_text = "attempt" if attempts == 1 else "attempts"
    print(f"Congratulations! \nYou guessed the right number in", 
        f"{attempts} {attempts_text}!")
    print(separator)
    

def play_again():
    """Asks the user if they want to play again and
    either restarts the game or ends it."""
    
    while True:
        replay = input("Play again: (y/n)? ").lower()
        if replay == 'y':
            clear_screen()
            all_game()
            break
        elif replay == 'n':
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Invalid input. Please type only 'y' or 'n'.")

def all_game():
    """Main game loop that runs the Bulls and Cows game."""
    
    separator = '-' * 47
    game_on = True
    number = secret_number()    
    attempts = 0
    
    while game_on:
        guessing = user_guess()
        if guessing.lower() == "q":
            print('quitting the game')
            sys.exit()
        elif len(guessing) != 4 or not guessing.isdigit():
            clear_screen()
            print("Invalid input. Please enter a 4-digit number,", 
                  "\n(or press 'q' to quit).")
            continue
        attempts += 1

        print(separator)
        bulls = calculate_bulls(number, guessing)
        cows = calculate_cows(number, guessing)

        print_results(nr_bulls, nr_cows)

        if nr_bulls == 4:
            print_winning_message(attempts)
            play_again()
            break

if __name__ == "__main__":
    print_initial_greeting()
    all_game()
