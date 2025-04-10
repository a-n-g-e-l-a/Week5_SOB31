# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

# I fixed: '==' to '=' for assignment and corrected the input syntax
year = int(input("Greetings! What is your year of origin? "))  # I fixed the input syntax 

# I added colon at the end of 'if' statement and used proper comparison operators
if year < 1900:  # I fixed: missing colon and wrong condition syntax (used && which is invalid in Python)
    print('Woah, that is the past!')  # Print message for the past

# I changed logical operator '&&' to 'and' (Python uses 'and' for logical comparisons)
elif year >= 1900 and year <= 2020:  # I used 'and' instead of '&&' and fixed the condition
    print("That's totally the present!")  # Print message for the present

# I added proper 'else' block and fixed condition
else:  # I fixed: replaced invalid 'elif' with 'else' as no further condition is necessary
    print("Far out, that's the future!!")  # I added: print message for future years
