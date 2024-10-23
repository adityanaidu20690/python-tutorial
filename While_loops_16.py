# while loop = execute some code WHILE some condition remains True
######################################################################
# name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")


##########################################################################
# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name") #infinite loop until you enter name 
#     name = input("Enter your name: ")
#     print(name)


###################################################

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative") #infinite loop until you enter age above zero 
#     age = int(input("Enter your age: "))
#     print(f"You are {age} years old")

######################################################################################

# food = input("Enter a food you like(q to quit): ")

# while not food == "q":
#     print("You did not enter your name") #infinite loop until you press q
#     food = input("Enter another food you like(q to quit): ")

# print("bye")

##########################################################################################

num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num >10:
    print(f"{num} is not valid") #infinite loop until you enter name 
    num = int(input("Enter a number between 1 to 10: "))

print(f"Your number is {num}")