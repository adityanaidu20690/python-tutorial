# Augmented Assignment Operators and Built-in Functions in Python

# Augmented Assignment Operators
# In Python, augmented assignment operators are shortcuts to change a variable's value.
# They allow you to perform an operation and save the new result in the same variable in one step.

# Example of Augmented Assignment Operators
# Initialize variable
friends = 0

# Using traditional assignment
friends = friends + 1
print(friends)  # Output: 1

# Using augmented assignment operator
friends += 1
print(friends)  # Output: 2

# Another example with subtraction
friends -= 1
print(friends)  # Output: 1

# Using division
friends = 5
friends /= 1
print(friends)  # Output: 5.0

# Using multiplication
friends *= 1
print(friends)  # Output: 5.0

# Using exponentiation
friends = 3
friends **= 2  # Find the square of 3
print(friends)  # Output: 9

# Built-in Functions
# Python provides various built-in functions that help perform common tasks.
# Below are examples of some useful built-in functions: round(), abs(), max(), and min().

# Using the round() Function
# The round() function in Python is used to round a floating-point number to a specified number of decimal places.
a = 3.14
print(round(a))  # Output: 3

# Using the abs() Function
# The abs() function in Python returns the absolute value of a number.
# The absolute value is the non-negative value of a number, regardless of its sign.
b = -2
print(abs(b))   # Output: 2
print(abs(a))   # Output: 3.14

# Using the max() Function
# The max() function in Python returns the largest item from an iterable or the largest of two or more arguments.
c = 45
print(max(a, b, c))  # Output: 45

# Using the min() Function
# The min() function in Python returns the smallest item from an iterable or the smallest of two or more arguments.
print(min(a, b, c))  # Output: -2
