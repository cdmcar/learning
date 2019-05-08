primes = []
factors = []

def isPrime(num):
    for l in range(2,55003,1):
        if l != num:
            if num % l == 0:
                return False
                break

    return True

for i in range(1,110000,1):
    if isPrime(i):
        primes.append(i)

print(primes)
print(len(primes))
print(primes[10001])
