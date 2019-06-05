def is_prime(number):
    i = 2
    while number % i != 0:
        if number == i:
            return number

        i = i + 1


def primary_generator(n):
    i: int = 1
    while i < n:
        if is_prime(i):
            yield i
        i = i + 1
