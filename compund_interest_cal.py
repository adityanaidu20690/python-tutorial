# how to calculate compund interest
# A: The amount of money accumulated after n years, including interest.
# P: The principal amount (the initial sum of money).
# r: The annual interest rate (decimal).
# n: The number of times that interest is compounded per year.
# t: The number of years the money is invested or borrowed.
# a= p* pow((1 + r/n), time)
# principle= input("enter the principle amount: ")
while principle <= 0:
    principle= int(input("enter the principle amount: "))
    if (principle <= 0):
        print("principle cannot be less than or equal to zero")
while rate <=0:
    rate=float(input("enter the interest rate value: "))
    if rate <=0:
        print("rate cannot be less than or equal to zero")
while time<=0:
    time=int(input("enter the time: "))
    if time<=0:
        print("time cannot be less than or equal to zero")

print(principle)
print(time)
print(rate)
total = principle * pow((1 + rate/100), time)
print ("the compound interest is {total}")