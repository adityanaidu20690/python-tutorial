# Python User Input Exercises
# This document presents a series of exercises that demonstrate user input and basic calculations in Python.

# Exercise 1: Personal Information
# In this exercise, we prompt the user to enter their name and age, then increment the age by one.

# Get user name and age
name = input("Enter your name: ")
age = int(input("Please enter your age: "))
age += 1  # Increment age by 1
print(f"My name is {name} and my age is {age}.")

# Exercise 2: Calculate the Area of a Rectangle
# This exercise calculates the area of a rectangle based on user-provided dimensions.

# Calculate the area of the rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}.")

# Exercise 3: Shopping Cart
# In this exercise, we create a simple shopping cart that calculates the total amount based on user input.

# Shopping cart
item = input("Enter the name of the product: ")
price = int(input("Enter the price of the product: "))
quantity = int(input("Enter the total number of products you would like to buy: "))
total = quantity * price
print(f"The total quantity purchased for the product '{item}' is: {quantity} x {item}.")
print(f"The total amount to be paid is: {total}.")
