#  Logical Operators in Python represented by lower case words
# 1. and
from doctest import Example

print( False and False ) # False
print( True and False ) # False
print( False and True ) # False
print( True and True ) # True
print("==========================")

# 2. or
print( False or False ) # False
print( True or False ) # True
print( False or True ) # True
print( True or True ) # True
print("==========================")

# 3. not
print( not True ) # False
print( not False) # True
print("==========================")

#Examples
a = 10
b = 20
print( a<b and b>a )   # True
print( not(a<b and b>a) )   # False
print("==========================")


# Logical Operators with other data types -->
# 0/0.0/None/"" --> False
# other values --> True

# Note1 --> if input1 is True, input2 is True, input2 will be result
print( "Hello" and "bye") # "Hello"(True) and "bye"(True) --> bye
print( "Hello" and 10) # "Hello"(True) and 10(True) --> 10
print( "Hello" and 10.5) # "Hello"(True) and 10.5(True) --> 10.5
print("=====================================================================")

# Note2 --> if input1 is True, input2 is False, input2 will be result
print( "Hello" and "" ) # "Hello"(True) and ""(False) --> Empty string
print( "Hello" and 0 ) # "Hello"(True) and 0(False) --> 0
print( "Hello" and 0.0 ) # "Hello"(True) and 0.0(False) --> 0.0
print( "Hello" and None ) # "Hello"(True) and None(False) --> None
print("=====================================================================")

# Note3 --> if input1 is False, input2 is True, input1 will be result
print( "" and "bye") # ""(False) and "bye"(True) --> empty string
print( 0 and 10) # 0(False) and 10(True) --> 0
print( 0.0 and 10.5) # 0.0(False) and 10.5(True) --> 0.0
print( None and 10.5) # None(False) and 10.5(True) --> None
print("=====================================================================")

# Note4 --> if input1 is False, input2 is False, input1 will be result
print( "" and 0 ) # ""(False) and  0(False) --> 0
print( 0 and 0.0 ) # 0(False) and 0.0(False) --> 0.0
print( 0.0 and "") # 0.0(False) and ""(False) --> Empty string
print( None and 0 ) # None(False) and None(False) --> None
print("=====================================================================")
