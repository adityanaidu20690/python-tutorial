# for x in range(3):
#     for y in range(8):
#         print (y, end='')
#     print()

rows= int(input("enter the value: "))
column= int(input("enter the value "))
symbol= input("enter the symbol:  ")
for x in range(rows):
    for y in range(column):
        print(symbol, end="")
    print()