

# Reading Global Variable
# -----------------------
x = 10
def read_only():
    y = x + 5  # just reading global x
    print(y)

read_only()
print("==============================================")

# Modifying/assigning a global variable
# -------------------------------------
# You must use global if you want to update the global variable inside the function. Otherwise, Python will treat x as a local variable
# x = 10
# def modify_wrong():
#     x = 20      # Error :: assignment → Python treats x as local
#     print(y)
# modify_wrong()
print("==============================================")

a = 10
def modify():
    global a    # now Python knows a is global
    a = 20
    print("Updated global a:", a)

modify()
print("Outside function global a:", a)
print("==============================================")


# When Local and global variable are with same name
id = 555
def variable_scope():
    id = 101
    age = 24
    print(f"Local Var id :: {id}") # 101
    print(f"Global Var id :: {globals()['id']}") # 555

    id = 202  # modifies local
    globals()['id'] = 888  # modifies global
    print(f"Updated Local id: {id}") # 202
    print(f"Updated Global id: {globals()['id']}") # 888

variable_scope()
print("==============================================")
print(f"Updated Global id outside function : {id}") # 888
