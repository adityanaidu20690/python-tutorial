######################################
###String Methods###################

# name = input("Enter your full name: ")
# result = len(name)
# print(result) #include spaces as length count (srikar babu) = 11

##########################################################

# name = input("Enter your full name: ")
# result = name.find(" ")
# print(result) 

#result
# Enter your full name: srikar babu
# 6

##############################################

# name = input("Enter your full name: ")
# result = name.find("r")
# print(result) # index value of r=1 in srikar (1st occurance)

###############################################


# name = input("Enter your full name: ")
# result = name.rfind("r")   #last occurance
# print(result) #index value of r=5 in srikar
#if it doesent find the value it shows '-1' as output  replacing r with z

#####################

# name = input("Enter your full name: ")
# name = name.capitalize()   #takes srikar babu as one string i.e., it only s will change
# print(name)

###############################################

# name = input("Enter your full name: ")
# name = name.upper()   #changes complete string, even it is has spaces srikar babu =SRIKAR BABU
# name = name.lower()  #lower case
# print(name)


#####################

# name = input("Enter your full name: ")

# result = name.isdigit()  #shows true only string has numbers, if it is mixed with any alphabet it results false
# print(result) #srik123 == False ## 12345 == True

##################################################

# name = input("Enter your full name: ")

# result = name.isalpha()  #shows true only string has alphabets, if it is mixed with any numbers or space it results false
# print(result)

#################################################

# phone_number = input("Enter your phone number: ")

# result = phone_number.count("-")  # counts number of '-' in the string
# print(result)

#############################


# phone_number = input("Enter your phone number: ")

# result = phone_number.replace("-", " ")  #replaces all the '-' with spaces
# print(result)

###################################################
# print(help(str))

###################################################
"""  Validate user input exercise
1. username is not more than 12 characters
2. username must not contain spaces
3. username must not contain digits  """



# username = input("Enter a username: ")

# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}")

#####################################################################

