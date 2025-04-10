# I added proper parentheses and colons, fixed logic issues
greeting = input("Hello, possible pirate! What's the password?")  # I added input for pirate password

# I fixed mismatched parentheses and incomplete condition
if greeting in ["Arrr!"]:  # I changed the incorrect list syntax (missed closing parenthesis)
    print("Go away, pirate.")  # I added this line to print if password matches "Arrr!"

# I fixed: 'elif' was incomplete, added correct condition and print statement
else:  # I added 'else' to handle the case when the password is not "Arrr!"
    print("Greetings, hater of pirates!")  # I added this line to greet non-pirates
