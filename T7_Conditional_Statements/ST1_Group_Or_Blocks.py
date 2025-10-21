

# Group or Blocks are classified into 2 types
#   1. indented block
#   2. inline block


# Indentation block
# -----------------
# 1.Every block of code must have the same number of spaces for each level.
#       * recommends 4 spaces per indentation level.
#       * Avoid mixing tabs and spaces — it leads to errors.
if False:
    print("Yes")
    print("Still inside")

print("No")



#  Simple if statement
# ---------------------
# Q. WAP to print given number in positive format
num = 25

if num<0:
    num *= (-1)
    print("Given number is converted to positive number")

print(f"Given number :: {num}")

# -----------------------------------------------------------------------------------
# Q. WAP to Check given number is Positive or negative
num = -25

if num>=0:
    print(f"{num} is a Positive number")
else:
    print(f"{num} is a Negative number")