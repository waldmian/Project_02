import os
separator = '-' * 40
# def user_guess():
#   while True:
#     user_guess_input = input(f"Enter a 4-digit number: \n{separator}\n>>> ")
#     #print(separator)
#     if user_guess_input.lower() == "q":
#       print('quitting the game')
#       break

#     elif len(user_guess_input) != 4 or not user_guess_input.isdigit():
#       os.system('cls')
#       print("Invalid input. Please enter a 4-digit number (or press 'q' to quit).")
#     else:
#       break
#   print(separator)
 

# user_guess()

def secret_number():
  return str(random.randint(1000, 9999))

def user_guess():
  return input(f"Enter a 4-digit number: \n{separator}\n>>> ") 

  def bulls_and_cows_formatting():
    nr_bulls = len(bulls)
    nr_cows = len(cows)

    bulls_text = "bull" if nr_bulls == 1 else "bulls"
    cows_text = "cow" if nr_cows == 1 else "cows"
    print(f"{nr_bulls} {bulls_text}, {nr_cows} {cows_text}")
