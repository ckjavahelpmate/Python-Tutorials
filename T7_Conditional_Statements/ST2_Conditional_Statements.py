
# Conditional statements control the flow of execution based on whether a condition is True or False
# In Python we have 4 Types
#   1. Simple if
x = 10
if x > 5:
    print(f"Given number {x} is greater than 5")
print("---------------------------------------------")

#   2. if-else
a = 10
b = 20
if a>b:
    print(f"Largest of {a} & {b} is {a}")
else:
    print(f"Largest of {a} & {b} is {b}")
print("---------------------------------------------")

#   3. if-elif-else
a = 80
b = 40
c = 20
if a>b and a>c:
    print(f"Largest of {a}, {b} & {c} is {a}")
elif b>a and b>c:
    print(f"Largest of {a}, {b} & {c} is {b}")
else:
    print(f"Largest of {a}, {b} & {c} is {c}")
print("---------------------------------------------")

#   4. match-case :: Executes only the first matching case block, No “fall-through” happens like switch case
choice = 2
match choice:
    case 1:
        print("You chose 1")
    case 2:
        print("You chose 2")
    case 3:
        print("You chose 3")
    case 4:
        print("You chose 4")
    case _:  # default case
        print("Invalid choice")
