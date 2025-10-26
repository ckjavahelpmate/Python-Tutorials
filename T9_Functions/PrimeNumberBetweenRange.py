
def is_prime(n):
    count=0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        if count>2:
            return False
    return count==2

def print_primes(start , end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)

start = int(input("Enter start range :: "))
end = int(input("Enter end range :: "))
print_primes(start, end)