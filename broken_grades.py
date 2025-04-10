# I added this function to ensure only valid integers are entered for exam grades
# Reason: Prevents program crashes when users input letters or invalid values
def get_grade(prompt):
    while True:
        try:
            grade = int(input(prompt))  # Try converting input to integer
            """
            'input()' function used for exam grades from the user.
            and input() returns a string then convert it to an integer using 'int()'
            then mathematical calculations can work.
            """
            return grade
        except ValueError:
            print("Invalid input. Only numbers are allowed.")  # Clear user message

# I fixed original input inconsistencies and used the safe input function instead of raw input()
exam_one = get_grade("Input exam grade one: ")         
exam_two = get_grade("Input exam grade two: ")         
exam_three = get_grade("Input exam grade three: ")     

# I fixed the variable name inconsistency (was: exam_3, grades list had syntax errors)
grades = [exam_one, exam_two, exam_three]  

# I added this: Corrected logic for summing the grades
# Reason: original loop was using 'grade' instead of 'grades' and overwrote the 'sum' function
total = 0
for grade in grades:
    total += grade # Simplified and corrected the accumulation logic

# I fixed typo: 'grdes' to 'grades' and renamed 'sum' to 'total' to avoid conflict with built-in
avg = total / len(grades)

# I fixed logic and syntax in conditional blocks (missing colons, invalid string quotes, wrong operators)
# Determining the letter grade

"""
'if', 'elif', 'else') used to check which range the 
average score falls into and assigns the appropriate grade.
"""

if avg >= 90:
    letter_grade = "A" # No change needed
elif avg >= 80:
    letter_grade = "B"  # I simplified condition: 'avg < 90' is not needed due to elif
elif avg > 69:
    letter_grade = "C"  # I fixed quote error ('C' -> "C")
elif avg >= 65:
    letter_grade = "D" # I changed condition from 'avg <= 69 and avg >= 65' to just 'avg >= 65'
else:
    letter_grade = "F"  # I fixed: added proper else block with condition fallback

# Printing results

"""
'for' loop is used to iterate over the 'grades' list 
and print each exam score separately.
"""

# I fixed the for-loop indentation and printing logic
# Reason: The original printed average and grade inside the loop by mistake
for grade in grades:
    print("Exam:", grade)  # I changed from string concatenation to comma

# I moved average and grade printing outside the loop
print("Average:", avg)
print("Grade:", letter_grade)

# I fixed: original used 'letter-grade is "F"' (invalid syntax)
# Changed to proper variable name and used '==' for comparison
if letter_grade == "F":
    print("Student is failing.") # I added parentheses 
else:
    print("Student is passing.") # I added parentheses
