# list
# A list will be under these brackets []. It is ordered and mutable, and we can add duplicate values.
# fruits= ['apple' , 'banana' , 'dragon', 'pineapple']
# for x in fruits:
#     print(x)

# print(dir(fruits))
# print(len(fruits)) #this will give the length of the fruits
# print("banana" in fruits) # this give the output in boolean format
# fruits[0]= "kiwi"#if you specify this it will replace apple with kiwi
# for x in fruits:
#     print(x)


#set 
# A set will be under {}. It is unordered and immutable (cannot be changed), but we can add or delete data. However, it does not allow duplicate values.
#If there are any duplicate values, the set will omit them and display the output without any duplicates.
# fruits ={'apple' , 'banana' , 'dragon', 'pineapple'}
# print (fruits)
# print(fruits.pop()) #this function will remove the first word from the set.
# print (fruits)
# fruits.clear()
# print (fruits)

#tuple 
#A tuple will be under (). It is ordered and immutable, and duplicate values are also allowed. 
fruits =('apple' , 'banana' , 'dragon', 'pineapple' , 'dragon' , 'apple')
print (fruits)

print("banana" in fruits) # this give the output in boolean format
fruits.index("dragon")
print(fruits.index("apple"))
