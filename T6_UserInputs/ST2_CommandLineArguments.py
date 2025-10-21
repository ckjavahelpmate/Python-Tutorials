import sys
from doctest import Example

# We can read the inputs from Command Line arguments
# step-1 :: we should import the "sys"
# step-2 :: call the "sys.argv[index]"
#  Note
#  1.Index starts from 0, and filename will be first argument
#  2.Every data is read as string only

# Example --> Demo.py Sheela 101 24
filename = sys.argv[0]
name = sys.argv[1]
id = int(sys.argv[2])
age = int(sys.argv[3])

print(f"Name :: {filename}") # Demo.py
print(f"Name :: {name}") # Sheela
print(f"Age :: {id}") # 101
print(f"ID :: {age}") #24


