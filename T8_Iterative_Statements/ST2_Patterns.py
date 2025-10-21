"""
Pattern-01
1   2   3   4
1   2   3   4
1   2   3   4
1   2   3   4
"""
n = 4
for i in range(n):
    for j in range(n):
        print(j+1, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-02
1   1   1   1
2   2   2   2
3   3   3   3
4   4   4   4
"""
n = 4
for i in range(n):
    for j in range(n):
        print(i+1, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-03
4   4   4   4
3   3   3   3
2   2   2   2
1   1   1   1
"""
n = 4
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(i, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-04
4   3   2   1
4   3   2   1
4   3   2   1
4   3   2   1
"""
n = 4
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(j, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-05
1
1   2
1   2   3
1   2   3   4
"""
for i in range(4):
    for j in range(0, i+1):
        print(j+1, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-06
            1
        1   2
    1   2   3
1   2   3   4
"""
n = 4
for i in range(n):
    for j in range(i, n-1):
        print("  ", end="")
    for j in range(0, i+1):
        print(j+1, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-07
1   2   3   4
1   2   3
1   2
1
"""
n = 4
for i in range(n):
    for j in range(1, n-i+1, 1):
        print(j, end=" ")
    print()
print("----------------------------------------")

"""
Pattern-08
1   2   3   4
    1   2   3
        1   2
            1
"""
n = 4
for i in range(n):
    for j in range(i):
        print("  ", end="")
    for j in range(1, n-i+1, 1):
        print(j, end=" ")
    print()
print("----------------------------------------")


"""
Pattern-09
        * 
      * * * 
    * * * * * 
  * * * * * * * 

"""
n = 4
for i in range(n):
    for j in range(n, i+1, -1):
        print("  ", end="")
    for j in range( i+1):
        print("*", end=" ")
    for j in range( i):
        print("*", end=" ")
    print()
print("----------------------------------------")

"""
Pattern-10
* * * * * * * 
  * * * * * 
    * * * 
      * 
"""
n = 4
for i in range(n):
    for j in range(i):
        print("  ", end="")
    for j in range(n, i, -1):
        print("*", end=" ")
    for j in range(n, i+1, -1):
        print("*", end=" ")
    print()
print("----------------------------------------")

"""
Pattern-11

      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
"""
n = 4
for i in range(n-1):
    for j in range(n, i+1, -1):
        print("  ", end="")
    for j in range( i+1):
        print("*", end=" ")
    for j in range( i):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i):
        print("  ", end="")
    for j in range(n, i, -1):
        print("*", end=" ")
    for j in range(n, i+1, -1):
        print("*", end=" ")
    print()
print("----------------------------------------")
