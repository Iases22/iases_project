"""
Generates primes up to a limit: will return all primes < 100 for any limit < 100,
else all primes up to and including the given limit
"""


def eratosthenes_sieve(limit):
    #create array
    array = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    ]
    lim = int(limit + 1)

    if lim <= 97:
        return array

    for i in range(98, lim):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0 and i % 29 != 0 and i % 31 != 0 and i % 37 != 0 and i % 41 != 0 and i % 43 != 0 and i % 47 != 0 and i % 53 != 0:
            array.append(i)

    #apply sieve
    for i in array:
        if i > int(limit**0.5):
            break
        for j in array[i + 1:]:
            if j % i == 0:
                array.remove(j)

    return array


def try_me():
    print('Prime numbers under 200: ')
    print(eratosthenes_sieve(200))
