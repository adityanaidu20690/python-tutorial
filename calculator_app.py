# Create a calculator app using nested if conditions in Python

# Prompt the user to enter the operator
operator = input("Please enter the operator (such as +, -, *, /): ")  # We are entering the operator here

# Prompt the user to enter the two numbers
num1 = float(input("Enter the first value: "))  # Enter the first value
num2 = float(input("Enter the second value: "))  # Enter the second value

# Perform the calculation based on the operator
if operator == '+':
    result = num1 + num2  # We are adding the two given numbers
    print(f"The result of {num1} + {num2} = {round(result)}")  # Display the result
elif operator == '-':
    result = num1 - num2  # We are subtracting the two given numbers
    print(f"The result of {num1} - {num2} = {round(result)}")  # Display the result
elif operator == '*':
    result = num1 * num2  # We are multiplying the two given numbers
    print(f"The result of {num1} * {num2} = {round(result, 2)}")  # Display the result rounded to 2 decimal places
elif operator == '/':
    # Nested if to handle division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")  # Inform the user about division by zero
    else:
        result = num1 / num2  # We are dividing the two given numbers
        print(f"The result of {num1} / {num2} = {round(result, 2)}")  # Display the result rounded to 2 decimal places
else:
    print("Please enter a valid operator.")  # Improved feedback for invalid operator
