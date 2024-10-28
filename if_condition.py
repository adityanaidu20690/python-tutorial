# Prompt the user to enter their year of birth
year_of_birth = int(input("Enter your year of birth (e.g., 2000): "))

# Calculate the current year
current_year = 2024

# Calculate the user's age based on the year of birth
age = current_year - year_of_birth

# Print the calculated age
print(f"Your age is {age}.")

# Check if the user is eligible to enter the club based on their age
if age >= 18:
    print(f"You are {age} years old and you are eligible to enter the club.")
else:
    # Calculate how many more years the user needs to wait to be eligible
    years_remaining = 18 - age
    print(f"You are not eligible; please wait for {years_remaining} years.")




# year=int(input("enter your DOB: "))
# year=2024-year
# print(year)
# if year>=18:
#     print(f"your age is {year} and you are elgible to enter the club")
# else:
#     # age= 2024-year
#     print(f"you are not elgible, please wait for {year} years ")

