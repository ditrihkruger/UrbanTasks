
import math
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
l = len(numbers)
primes = []
not_primes  = []
for i in range(l):
    k = numbers [i]
    if k == 1:
        continue
    is_prime = True
    for d in range (2, int(math.sqrt(k))+1) :
        if k % d == 0 :
            is_prime = False
            not_primes.append(k)
            break
    if is_prime:
        primes.append(k)

print (primes)
print (not_primes)


