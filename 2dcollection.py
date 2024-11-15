# fruits = ["apple" , "banana" , "Chickoo"]
# vegetables= ["beans" , "capsicum" , "onion"]
# meat = ["fish" , "goat" , "chicken"]


# items=[fruits , vegetables , meat]
# for collection in items:
#     for food in collection:
#         print(food, end= ' ')
#     print()

num_pad = ((1,2,3),(4,5,6),(7,8,9),("*" , 0 , "#"))
for row in num_pad:
    for num in row:
        print(num, end= ' ')
    print()

print("#################################")

num_pad = [(1,2,3),(4,5,6),(7,8,9),("*" , 0 , "#")]
for row in num_pad:
    for num in row:
        print(num, end= ' ')
    print()