import random

# I added: Compare the user's guess to the number and count cows and bulls
def compare_numbers(number, user_guess):
    cows = 0  # I added: Initialize cows count
    bulls = 0  # I added: Initialize bulls count

    # I fixed: Loop through the number and guess to compare digits
    for i in range(len(number)):  
        if user_guess[i] == number[i]:  # I fixed: Check if digit is in the correct position
            bulls += 1  # I added: Increment bulls if the digit is correct in the correct position
        elif user_guess[i] in number:  # I fixed: Check if the digit exists elsewhere in the number
            cows += 1  # I added: Increment cows if the digit exists but in the wrong position

    return (cows, bulls)  # I added: Return cows and bulls as a tuple

# Game setup
playing = True  # I added: Start the game loop
number = str(random.randint(0, 9999)).zfill(4)  # I fixed: Ensure the number is always 4 digits
guesses = 0  # I added: Initialize guesses count

# I added: Game instructions
print("Let's play a game of Cowbull!")
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow.")
print("For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

# Main game loop
while playing:
    user_guess = input("Give me your best guess! (4 digits)")  # I fixed: Used input() to capture user guess
    if user_guess == "exit":  # I added: Option to exit the game
        print("Thanks for playing!")
        break  # Exit the game loop

    # I fixed: Check if the guess is a valid 4-digit number
    if len(user_guess) != 4 or not user_guess.isdigit():
        print("Invalid input. Please enter a 4-digit number.")  # I added: Print an error message for invalid input
        continue  # I added: Ask for input again if it's invalid

    cowbullcount = compare_numbers(number, user_guess)  # I fixed: Get the cows and bulls count
    guesses += 1  # I added: Increment the guess count

    print(f"You have {cowbullcount[0]} cows, and {cowbullcount[1]} bulls.")  # I fixed: Display cows and bulls correctly

    # I fixed: End the game if the user gets 4 bulls
    if cowbullcount[1] == 4:
        playing = False  # I added: Stop playing when 4 bulls are achieved
        print(f"You win the game after {guesses} guesses! The number was {number}.")
        break  # I added: Exit the game loop

    else:
        print("Your guess isn't quite right, try again.")  # I added: Prompt the user to try again if not correct
