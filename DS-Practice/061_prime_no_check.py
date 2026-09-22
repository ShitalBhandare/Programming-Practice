
'''
Write a program to find the first 50 prime numbers.

Approach
Initialize a list to store prime numbers.
Start checking from the first prime candidate (2) upwards.
For each candidate, check divisibility only up to its square root to determine if it is prime.
If prime, add it to the list.
Repeat until the list contains 50 prime numbers.


'''

def first_50_primes():
    primes = []
    num = 2
    while len(primes) < 50:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

print(first_50_primes())
