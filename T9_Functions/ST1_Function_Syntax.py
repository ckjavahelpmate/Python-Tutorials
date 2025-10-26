#Fuctions Rules
# ----------------
# 1. You must use the def keyword to define a function
# 2. Function definition must be followed by parentheses () and a colon :.
# 3. The body must be indented (4 spaces is standard).
# 4. Use snake_case for function names (lowercase with underscores).

# Syntax :
# ----------------------------
# def function_name(parameters):
#     statement(s)
#     return value   # optional

# Types of Parameters
# -------------------
# 1. Positional Parameters      --> Must be passed in the same order as defined
def add(a, b):
    print(a + b)

add(5, 3)
print("=================================================================")

# 2. Default Parameters         --> Have default values if no argument is provided
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # uses default
greet("Alice")    # overrides default
print("=================================================================")

# 3. Keyword Parameters         --> Passed by name, order doesn’t matter
def student_info(name, grade):
    print(f"{name} is in grade {grade}")

student_info(grade=5, name="Ravi")  # order reversed, still works
print("=================================================================")

# 4. Variable-length Positional --> Accepts any number of positional arguments
def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

add_numbers(2, 3, 5)
add_numbers(1, 2, 3, 4, 5)
print("=================================================================")

# 5. Variable-length Keyword    --> Accepts any number of keyword arguments as a dictionary
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_profile(name="Alice", age=25, country="India")
print("=================================================================")



