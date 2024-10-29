# format specifiers = {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate the mnay spaces
# :<=left justify
#:> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value 
# := =place sign to leftmist position
# : = insert a space before positive numbers
# :, = comma separator

price1= 3.14159
price2= -987.65
price3= 12.34
print(f"price 1 is ${price1:^2f}")