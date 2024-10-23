# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive Value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

############################################################
# price1 = 3.14159
# price2 = -987.652
# price3 = 12.34

# print(f"Price 1 is ${price1:.2f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.2f}")
#####result#########
# Price 1 is $3.14
# Price 2 is $-987.65
# Price 3 is $12.34
####################

############################################################################


# price1 = 3345.14159
# price2 = -9837.652
# price3 = 1224.34

# print(f"Price 1 is ${price1:7}")
# print(f"Price 2 is ${price2:2}")
# print(f"Price 3 is ${price3:2}")

# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")


# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}") #try the same with < > ^
#####result#########
# Price 1 is $3345.14159
# Price 2 is $-9837.652
# Price 3 is $1224.34
# Price 1 is $ 3345.14159
# Price 2 is $-9837.652
# Price 3 is $ 1224.34
# Price 1 is $+3,345.14
# Price 2 is $-9,837.65
# Price 3 is $+1,224.34
