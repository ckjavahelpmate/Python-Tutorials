
#  We can read the input from console using
#  1. input()
#  2. input(String message)
# Note :: Every data is read as string only

# Example
# Read String
studentName = input("enter student Name :: ")

# Read int
studentId = int(input("enter student Id :: "))
studentAge = int(input("enter student Age :: "))

# Read float
studentStipend = float(input("enter student stipend :: "))

print(f"ID :: {studentId}")
print(f"Name :: {studentName} ")
print(f"Age :: {studentAge}")
print(f"stipend :: {studentStipend}")


#  To read an expression --> eval(expression)
# Example input --> 3+2*4
result = eval( input("enter expression :: ") )
print(f"Expression result :: {result}") # 11



