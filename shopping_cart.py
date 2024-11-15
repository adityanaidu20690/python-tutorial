foods=[]
prices=[]
total = 0
while True:
    food= input("enter the food item (q to quit): ")
    if food.lower() == 'q':
        print("Thank you for shopping")
        break
    else:
        price= float(input(f"the price for the {food} you have selected is: "))
        foods.append(food)
        prices.append(price)
print("--------------------------Your Cart------------------")


for food in foods:
    print(food , end=" ")
for price in prices:
    total += price
print(f"you total is : {total}")