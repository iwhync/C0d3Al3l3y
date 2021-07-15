from sympy import sieve
import re
x = input("input: ")
x = re.findall(r"[0-9.-]+",x)
x = [int(x) for x in x]
z = x.pop(0)
primes = list(sieve.primerange(0,20000000))
for num in range(z):
    p = x.pop(0)-1
    print(primes[p])
