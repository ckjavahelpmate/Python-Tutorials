
# Python is dynamically typed language --> data type changes dynamically
x = 10.5
z =  10
print(f"var x :: {x}") # 10.5
print(f"var y :: {z}") # 10
print("==========================================")

z=x
print(f"var x :: {x}") # 10.5
print(f"var y :: {z}") # 10.5
print("==========================================")

# we can check data type of variable by type(value) function
a = "Hello"
print(f"var a :: {a}") # Hello
print(type(a)) # <class, 'str'>
print("==========================================")

# Convert other data types to int
print( int(10.6) ) # 10 --> float ~ int
print( int("202") ) # 202 --> String ~ int
print( ord("A") ) # 65 --> char ~ ASCII
print( int(True)) # 1
print( int(False)) # 0

print("==========================================")
# Convert other data types to float
print( float(10) ) # 10.0 --> int ~ float
print( float("10.6") ) # 10.6 --> String ~ float
print( float(ord("A") ) ) # 65 --> char ~ ASCII ~ float
print( float(True)) # 1.0
print( float(False)) # 0.0

print("==========================================")
# Convert other data types to String
print( str(10) )
print( str(10.6) )
print( str(True))
print( str(False))

print("==========================================")
# Convert other data types to Boolean
print( bool("True") ) # True
print( bool("df") ) # True
print( bool('False') )  # True — because any non-empty string is True
print( bool("") )  # False

