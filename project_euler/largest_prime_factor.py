
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

primes = []
factors = []

def isPrime(num):
    for l in range(2,100,1):
        if l != num:
            if num % l == 0:
                return False
                break

    return True

for i in range(1,100000,1):
    if isPrime(i):
        primes.append(i)

for i in primes:
    if 600851475143 % i == 0:
        factors.append(i)

print(factors)
