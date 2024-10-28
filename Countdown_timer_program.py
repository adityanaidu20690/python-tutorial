# import time

# time.sleep(3)

# print("Time's up!")


#############################################

# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(0, my_time):
#     print(x)
#     time.sleep(x)

# print("Time's up!")

########################################################

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")