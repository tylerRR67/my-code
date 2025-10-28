# This program tells you if a number is odd or even

# Ask the user for a number
number = input("Enter a number: ")

# Make sure the input is a number
if number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
    number = int(number)

    # Check if it's even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
else:
    print("Please enter a valid whole number.")
