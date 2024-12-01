import math
import itertools

def prime_factors(n):
    while n % 2 == 0:
        yield 2
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i== 0:
            yield i
            n = n // i
    if n > 2:
        yield n

def divisors(number):
    primes = list(prime_factors(number))
    x = [math.prod(l) for l in itertools.combinations(primes, 1)]
    for i in range(2, len(primes) + 1):
        x += [math.prod(l) for l in itertools.combinations(primes, i)]
    x = list(set(x))
    x.append(1)
    x.sort()
    return x
