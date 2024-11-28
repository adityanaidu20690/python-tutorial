# For right angle triangle:
for i in range(5):
    for j in range(i + 1):
        print("*" , end=' ')
    print()
print('###############################################')
# Print a downward half-pyramid pattern of stars
for i in range(5):
    for j in range(i , 5):
        print('*' , end=' ')
    print()
print('###############################################')
# print a triangle starting from top right
for i in range(5):
    for j in range(i , 5):
        print(' ', end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
print('###############################################')
for i in range(5):  # Loop for i from 0 to 4
    for j in range(i+1):  # Inner loop 1: prints empty spaces, depending on the value of i
        print("", end="")  # Prints nothing (empty space)
    
    for j in range(i, 5):  # Inner loop 2: prints '*' characters
        print('*', end=" ")  # Prints '*' followed by a space
    
    print()  # Prints a newline after each row

print('############################################')
# hill pattern
for i in range(5):
    for j in range(i , 5):
        print(' ', end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

print('############################################')
# reverse hill pattern
n=5
for i in range(n):
    for j in range(i+1):
        print(' ', end=" ")
    for j in range(i, n-1):
        print('*', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()


