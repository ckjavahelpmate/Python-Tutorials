

# String
# ==========
# A string in Python is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or even triple quotes (''' ''' or """ """).
# Strings are immutable
# You can index, slice, iterate, and concatenate strings.


# 1. Creating Strings
# =====================
str1 = 'Hello'
print(f"str1 = {str1}")

str2 = "Python"
print(f"str2 = {str2}")

str3 = '''Multi-line
string example'''
print(f"str3 = {str3}")

str4 = """Multi-line
string example"""
print(f"str4 = {str4}")

str5 = str(123)
print(f"str5 = {str5}")
print("=========================================")


# 2. String Indexing and Slicing
# ================================
# Strings are sequences, so you can access characters by index and extract parts using slicing.
# Examples :

s = "Python"
print(s[0])     # P (first character)
print(s[-1])    # n (last character)
print(s[0:4])   # Pyth --> start index is inclusive but end index is exclusive
print(s[2:])    # thon
print(s[1:3])    # Pyt --> start index is inclusive but end index is exclusive
print(s[::-1])  # nohtyP (reversed string)

print("============================================")

# 3. String Operations
# ==================
# 1. Using Operators
#       * we can use +, * , >, < , >=, <=, ==, !=, in
# EXamples :
str1 = "Hi"
str2 = "Sheela"
print( str1 + str2 )  # HiSheela --> Joins Strings
print( str1 , str2 )  # Hi Sheela --> Joins Strings separated by space
print( str1 * 3 ) # HiHiHi --> repeats the string for given times
print( str1 > str2 ) # False --> Compares lexicographically

print( "She" in str2 ) # true --> Checks "he" present in str2
print( "Sha" in str2 ) # false
print("============================================")

# 2. Using built-in functions
# | Function      | Description                                               | Example                                              |
# | ------------- | --------------------------------------------------------- | ---------------------------------------------------- |
# | `len()`       | Returns the length of a string                            | `len("Python") → 6`                                  |
# | `max()`       | Returns the highest (lexicographically largest) character | `max("Python") → 'y'`                                |
# | `min()`       | Returns the lowest (lexicographically smallest) character | `min("Python") → 'P'`                                |
# | `sorted()`    | Returns a sorted list of characters                       | `sorted("cat") → ['a','c','t']`                      |
# | `reversed()`  | Returns an iterator that accesses characters in reverse   | `''.join(reversed("abc")) → 'cba'`                   |
# | `enumerate()` | Returns index and character pairs                         | `list(enumerate("abc")) → [(0,'a'),(1,'b'),(2,'c')]` |
# | `chr()`       | Converts an integer (Unicode code point) to a character   | `chr(97) → 'a'`                                      |
# | `ord()`       | Converts a character to its Unicode code point            | `ord('a') → 97`                                      |
# | `str()`       | Converts another data type to a string                    | `str(123) → '123'`                                   |
# | `format()`    | Formats strings (similar to `.format()` method)           | `format(3.1415, ".2f") → '3.14'`                     |
# | `type()`      | Returns the type of a variable                            | `type("hello") → <class 'str'>`                      |
# | `dir()`       | Lists all available attributes/methods of a string        | `dir(str)`                                           |
# | `help()`      | Displays documentation of string functions                | `help(str.upper)`                                    |
# | `any()`       | Returns True if any element in iterable is True           | `any(c.isdigit() for c in "abc3") → True`            |
# | `all()`       | Returns True if all elements in iterable are True         | `all(c.isalpha() for c in "abc") → True`             |

print("============================================")

# 3. Using String Specific methods
# | Category           | Examples                                                                   |
# | ------------------ | -------------------------------------------------------------------------- |
# | Case Conversion    | `.lower()`, `.upper()`, `.capitalize()`, `.title()`, `.swapcase()`         |
# | Search & Replace   | `.find()`, `.replace()`, `.count()`, `.index()`, `.rfind()`                |
# | Whitespace         | `.strip()`, `.lstrip()`, `.rstrip()`                                       |
# | Split & Join       | `.split()`, `.join()`, `.partition()`, `.splitlines()`                     |
# | Checks (Boolean)   | `.isalpha()`, `.isdigit()`, `.islower()`, `.isupper()`, `.isspace()`, etc. |
# | Padding/Align      | `.center()`, `.ljust()`, `.rjust()`, `.zfill()`                            |
# | Encoding/Translate | `.encode()`, `.translate()`, `str.maketrans()`                             |


#  Examples
str = "Python Tutorials"
# Case Conversion
# ================================================
print(str.isupper()) # false
print(str.islower()) # false
print(str.istitle()) # True
print("============================================")
print(str.isalpha() ) # True
print(str.isnumeric() ) # False
print("1233".isnumeric() ) # True
print("============================================")

# Search & Replace
# =================================================
# 1. string.find(substring, start, end)
print( str.find("t") ) # 2  --> Returns the index of given character in string

# 2. string.replace(old, new, count)
print( str.replace("t", "f") ) # Pyfhon Tuforials

# Replace Multiple Different Characters (Using Regex)
# re.sub(pattern, repl, string, count=0, flags=0)
import re
text = "Dinga143@Dingi"
clean = re.sub(r'[0-9]', '*', text)
print(clean)

# 3. string.count(substring, start, end)
print( str.count("t") )

# 4. string.rfind(substring, start, end)
print( str.rfind("t") ) # 9 --> Returns the index of given character in string, check from right side

# 5. string.strip(chars)
text = "   Hello World   "
print(text.strip()) # Hello World --> Removes spaces from both ends.

# 6. string.split(separator, maxsplit)
text = "Python is fun"
result = text.split()
print(result) # ['Python', 'is', 'fun'] -> By default, .split() splits the string by spaces, tabs, and newlines

data = "2025-10-22"
print(data.split("-")) # ['2025', '10', '22']

# You can limit the number of splits.
text = "Python is easy to learn"
print(text.split(" ", 2)) # ['Python', 'is', 'easy to learn'] -> Only the first 2 spaces are used for splitting.

# Using re.split() for Multiple Separators
# import re
# re.split(pattern, string)
import re
text = "apple, banana orange,grape"
result = re.split(r'[ ,]', text)  # split on space or comma
print(result)


# 7. separator.join(iterable)
fruits = ["apple", "banana", "cherry"]
result = ",".join(fruits)
print(result) # apple,banana,cherry

numbers = ["2025", "10", "22"]
date = "-".join(numbers)
print(date) # 2025-10-22


print("============================================")

















