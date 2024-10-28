# Python String Methods Documentation

# 1. Convert all characters in the string to lowercase
string = "HELLO, WORLD!"
print(string.lower())  # Output: hello, world!

# 2. Convert all characters in the string to uppercase
string = "hello, world!"
print(string.upper())  # Output: HELLO, WORLD!

# 3. Convert the first character of each word to uppercase
string = "hello, world!"
print(string.title())  # Output: Hello, World!

# 4. Remove leading and trailing whitespace from the string
string = "   Hello, World!   "
print(string.strip())  # Output: Hello, World!

# 5. Replace occurrences of a substring with another substring
string = "Hello, World!"
print(string.replace("World", "Python"))  # Output: Hello, Python!

# 6. Split the string into a list of substrings based on the specified separator
string = "Hello, World!"
print(string.split(", "))  # Output: ['Hello', 'World!']

# 7. Join elements of an iterable into a single string, separated by the specified string
words = ["Hello", "World"]
print(", ".join(words))  # Output: Hello, World

# 8. Return the lowest index of the substring if found, otherwise returns -1
string = "Hello, World!"
print(string.find("World"))  # Output: 7
print(string.find("Python"))  # Output: -1

# 9. Return the number of occurrences of a substring in the string
string = "Hello, World! Hello, Python!"
print(string.count("Hello"))  # Output: 2

# 10. Returns True if the string starts with the specified prefix
print(string.startswith("Hello"))  # Output: True
print(string.startswith("Python"))  # Output: False

# 11. Returns True if the string ends with the specified suffix
print(string.endswith("!"))  # Output: True
print(string.endswith("Python"))  # Output: False

# 12. Capitalizes the first character of the string
string = "hello, world!"
print(string.capitalize())  # Output: Hello, world!

# 13. Returns True if all characters in the string are digits
string = "12345"
print(string.isdigit())  # Output: True
string = "1234abc"
print(string.isdigit())  # Output: False

# 14. Returns True if all characters in the string are alphabetic
string = "Hello"
print(string.isalpha())  # Output: True
string = "Hello123"
print(string.isalpha())  # Output: False

# 15. Returns True if all characters in the string are alphanumeric
string = "Hello123"
print(string.isalnum())  # Output: True
string = "Hello 123"
print(string.isalnum())  # Output: False

# 16. Swaps the case of all characters in the string
string = "Hello, World!"
print(string.swapcase())  # Output: hELLO, wORLD!

# 17. Formats the string using placeholders
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.
