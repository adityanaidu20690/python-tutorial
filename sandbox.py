
# link for the exercise: https://pynative.com/python-basic-exercise-for-beginners/
# Exercise 1: Calculate the multiplication and sum of two numbers
x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))
print("###############################")
print(f"the value of x is: {x}")
print("###############################")
print(f"the value of y is: {y}")
print("###############################")

print(f"The addition of {x} and {y} is: {x + y}" )
print("###############################")
print(f"The multiplication of {x} and {y} is: {x* y}" )

# Exercise 2: Print the Sum of a Current Number and a Previous number
previous_number=0
for i in range(1,10):
    x_sum=previous_number + i
    
    print(f"the value of previous_number is {previous_number} and the sum of previous and current number is {x_sum}")
    previous_number=i

# Exercise 3: Print characters present at an even index number
x="alphabets"
for i in range(len(x)):
    if i%2==0:
        print(x[i])

# Exercise 4: Remove first n characters from a string
x= str(input("Enter the string: "))
n =int(input("enter the value to be omitted from the string: "))
print(f"The given string is : {x}")
print(f"The given value of n is : {n}")
print(x[n:])

# Exercise 5: Write a code to return True if the list's first and last numbers are the same . if the numbers are different, return false.
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
a=numbers_x[::-1]
b=numbers_y[::-1]
if numbers_x[0]==a[0]:
    print("true")
else:
    print("false")
if numbers_y[0]==b[0]:
    print("true")
else:
    print("false")

# Exercise 6: Display numbers divisible by 5
set= [12 , 14 , 16 , 20 , 24 , 25]
for i in set:
    if i%5==0:
        print(f"{i} is divisible by 5")
# Exercise 7: Find the number of occurrences of a substring in a string
str_x = "Emma is good developer. Emma is a writer"
x=str_x.count("Emma")
print(x)

# Exercise 8: Print the following pattern
for num in range(6):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")

# Exercise 9: Check Palindrome Number
number= input("enter the value: ")
x=str(number)[::-1]
if str(number) == x :
    print("it is a palindrome")
else:
    print("not a palindrome")

# Exercise 10: Merge two lists using the following condition
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
final_list=[x for x in list1 if x%2==1] #ternery operator where we are only taking the odd values
final_list2=[y for y in list2 if y%2==0]
final_list.extend(final_list2)# we are joining both lists here
print(final_list)

# Exercise 11: Get each digit from a number in the reverse order.
x=4567
x=str(x)
print(' '.join(x[::-1]))

# Exercise 12: Calculate income tax
per=int(input("enetr the percentage% to be calculated: "))
number=int(input("enter the number: "))
percentage= (per/100)*number
per2=int(input("enetr the 2nd percentage% to be calculated: "))
number2=int(input("enter the 2nd number: "))
percentage2= (per2/100)*number2
print(percentage+ percentage2)

# Exercise 13: Print multiplication table from 1 to 10
for i in range(1,11):
    
    for j in range(1 , 11): 
        print(i*j , end= " ") 
    print()

#Exercise 14: Print a downward half-pyramid pattern of stars
for i in range(5):
    for j in range(i , 5):
        print('*', end=' ')
    print()

# Exercise 15: Get an int value of base raises to the power of exponent
import math
number=5
base=4

square=int(math.pow(number,base))
print(square)


