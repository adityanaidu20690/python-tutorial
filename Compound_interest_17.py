#python compound interest

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("enter the principle amount:  "))
    if principle <= 0:
        print("principle can't be less than or equal to zero")
#####################another method#####################
# while True:
#     principle = float(input("enter the principle amount:  "))
#     if principle <= 0:
#         print("principle can't be less than or equal to zero")
#     else:
#         break
###############################################################

while rate <=0:
    rate = float(input("enter the Interest rate:  "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")



while time <=0:
    time = float(input("enter the Time in years:  "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")