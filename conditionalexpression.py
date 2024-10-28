# Program to check if a number is positive, negative, or zero using the ternary operator

# Syntax for the ternary operator:
# result = X if condition else Y

# Prompt the user to enter a number
number = int(input("Enter a number: "))  # Input the number to be checked

# Determine if the number is positive, negative, or zero using the ternary operator
result = "positive" if number > 0 else "negative" if number < 0 else "zero"

# Output the result
print(f"The number is {result}.")  # Display the result
