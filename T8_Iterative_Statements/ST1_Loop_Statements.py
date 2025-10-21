

# Iterative statements are used to repeat a block of code multiple times until a certain condition is met.
# In Python we have 2 main loop statements
#   1. While loop
# Syntax :
#             while condition:
#                     block of statements
# Example :
num = 1
while num <= 5:
    print(num)
    num += 1

print("----------------------------------------")

#   2. for loop
# Syntax :
#           for variable in sequence
#                 block of statements
# Example :
for num in range(5):
    print(num+1)
print("----------------------------------------")

for ch in "Programmer":
    print(ch, end=", ")

print("\n----------------------------------------")

# else block can be used with loop statements
# The else block with a loop runs only if the loop wasn’t terminated by a break.
# It’s not tied to whether the condition was true or false, It’s about how the loop ended.
# Example
num = temp = 12345
key = 8
while num>0:
    if num%10 == key:
        print( f"{key} is present at {temp}")
        break
    num //=10
else:
    print(f"{key} is not present at {temp}")

print("----------------------------------------")

# What is range()?
# range() is built in function to generate sequence numbers
# Syntax :
# 1. range(stop) --> stop is exclusive
print( list(range(5)) )

# 2. range(start, stop) --> start is inclusive but stop is exclusive
print(  list(range(5,10)) )

# 3. range(start, stop, step) --> start is inclusive but stop is exclusive
print( list(range(10, 20, 2)) ) # 10, 12, 14, 16, 18
print( list(range(20, 10,-2)) ) # 20, 18, 16, 14, 12






