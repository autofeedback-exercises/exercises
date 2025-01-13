def isPrime(x):
    from math import sqrt, ceil
    if (x == 2) or (x == 3):
        return True
    if (x == 1) or (x % 2 == 0):
        return False
    for ii in range(3, ceil(sqrt(x))+2):
        if (x % ii) == 0:
            return False
    return True

def primeList(N):
    primes = []
    for n in range(2, N+1):
        if (all(n % i for i in range(2, int(n ** 0.5) + 1))):
            primes.append(n)
    return primes

def primeFactors(N):
    primes = primeList(N)
    val = N
    decomposition = []
    for prime in primes:
        while (val % prime == 0):
            decomposition.append(prime)
            val = val/prime
    return decomposition
