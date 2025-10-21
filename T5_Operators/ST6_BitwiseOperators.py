
# Integer can be represented in 4 ways
#  1. Decimal Number        --> Prefix with None
decimaNumber = 12
print(decimaNumber) # 12 -> output type is decimal

#  2. Octal Number          --> Prefix with 0o
octalNumber = 0o12
print(octalNumber) # 10 -> output type is decimal

#  3. Hexadecimal Number    --> Prefix with 0x
hexadecimalNumber = 0x12
print(hexadecimalNumber) # 18 -> output type is decimal

#  4. Binary Number         --> Prefix with 0b
binaryNumber = 0b10
print(binaryNumber) # 2 -> output type is decimal
print("=====================================================")

#  1. we can Convert Decimal to Binary by "bin(value) : String"
binaryNumber = bin(10)
print(binaryNumber) # 0b1010

#  2. we can Convert Decimal to Octal by "oct(value) : String"
octalNumber = oct(12)
print(octalNumber) # 0o14

#  3. we can Convert Decimal to hexadecimal by "hex(value) : String"
hexadecimalNumberNumber = hex(18)
print(hexadecimalNumberNumber) # 0x12

print("=================================================")

# Bitwise Operators
# bitwise Operators works only with int and boolean data types
# 1. bitwise and [ & ] --> returns true when both inputs are true, else false
print( 4 & 5 ) # 4
print( 6 & 5 ) # 4
print( 7 & 5 ) # 5
print( False & False ) # False
print( False & True ) # False
print( True & False ) # False
print( True & True ) # True
print("=================================================")

# 2. bitwise or [ | ] --> returns true when any one input is true, else false
print( 4 | 5 ) # 5
print( 6 | 5 ) # 7
print( 7 | 5 ) # 7
print( False | False ) # False
print( False | True ) # True
print( True | False ) # True
print( True | True ) # True
print("=================================================")

# 3. bitwise xor [ ^ ] --> returns true when both inputs are different else false
print( 4 ^ 5 ) # 1
print( 6 ^ 5 ) # 3
print( 7 ^ 5 ) # 2
print( False ^ False ) # False
print( False ^ True ) # True
print( True ^ False ) # True
print( True ^ True ) # False
print("=================================================")

# 4. bitwise leftshift [ << ] --> moves the binary to left for given times
print( 3<<1 ) # 6
print( 3<<2 ) # 12
print( 3<<4 ) # 48
print( False<<False ) # 0
print( False<<True ) # 0
print( True<<False ) # 1
print( True<<True ) # 2
print("=================================================")

# 5. bitwise rightshift [ >> ] --> moves the binary to right for given times
print( 50>>1 ) # 25
print( 50>>2 ) # 12
print( 50>>3 ) # 6