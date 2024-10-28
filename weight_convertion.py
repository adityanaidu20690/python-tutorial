# Writing a Python program to convert weight from kilograms to pounds

# Prompt the user to enter their weight
weight = float(input("Enter your weight: "))  # Enter the weight to be converted
unit = input("Enter the unit for conversion (K for Kilograms or L for Pounds): ")  # Specify the unit

# Check the conversion type
if unit.upper() == 'K':  # Convert to pounds
    print("We are converting from kilograms to pounds.")
    weight = weight * 2.20462  # Conversion formula
    print(f"The converted weight in pounds is: {round(weight, 2)}")  # Display result rounded to 2 decimal places
elif unit.upper() == 'L':  # Convert to kilograms
    print("We are converting from pounds to kilograms.")
    weight = weight / 2.20462  # Conversion formula
    print(f"The converted weight in kilograms is: {round(weight, 2)}")  # Display result rounded to 2 decimal places
else:
    print("Please enter a valid unit (K for Kilograms or L for Pounds).")  # User feedback for invalid input
