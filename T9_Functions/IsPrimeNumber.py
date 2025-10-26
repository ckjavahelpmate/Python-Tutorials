
def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count += 1
        if count > 2:
            break
    if count == 2:
        print(f"{num} is prime Number")
    else:
        print(f"{num} is not prime Number")

is_prime(1)
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5)
is_prime(6)
is_prime(7)
is_prime(8)
is_prime(9)

# --------------------------------------------

def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count += 1
        if count > 2:
            return False
    return count==2

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))

# -----------------------------------



