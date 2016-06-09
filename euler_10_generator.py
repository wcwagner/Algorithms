#Add up all the prime numbers that are less than 2,000,000
import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False
    if number == 1:
        return False
    elif number == 2:
        return True

def get_primes_gen(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def sum_of_primes():
    total = 0
    for prime in get_primes_gen(2):
        if prime < 2000000:
            total += prime
        else:
            print total
            return

print sum_of_primes()
