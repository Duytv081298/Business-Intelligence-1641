import numpy as np

my_list = list(np.random.randint(-100, 100, size=100))

print("Original list: ", my_list)

my_list = list(map(lambda x: -x if x < 0 else x, my_list))

print("Positive list: ", my_list)


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                return False
        return True

# test
print("Primes < 100: ", list(filter(is_prime, range(0, 100))))

primes = sorted(list(set(filter(is_prime, my_list))))
print("Primes in my_list: ", primes)

# d)
for p in primes:
    div_p = list(filter(lambda x: True if x % p == 0 else False, my_list))
    print("[{0}]: {1}".format(p, div_p))

# generate odd number


def odd_gen():
    a = 1               # a0 = 1
    while True:
        yield a
        a = a + 2       # an = a(n-1) + 2


def get_n_generator(n, generator):
    i = 0
    for it in generator():
        if i == n:
            return it
        i = i + 1


print("Odd {0}th: {1}".format(5, get_n_generator(5, odd_gen)))


def pyramidal_gen():
    i = 0
    pyn = 0                 # pyn(0) = 0
    while True:
        yield pyn
        i = i + 1
        pyn = pyn + i**2    # pyn(n) = pyn(n-1) + n^2


print("Pyramidal {0}th: {1}".format(5, get_n_generator(5, pyramidal_gen)))


def bessel_array(x, n):
    if n == 0:
        return np.sin(x) / x
    elif n == 1:
        return np.sin(x) / (x**2) - np.cos(x) / x
    elif n == 2:
        return ((3 / (x**2) - 1) * np.sin(x)) / x - 3 * np.cos(x) / (x**2)
    else:
        raise ValueError  # throw exception


def bessel_gen(x, n):
    j0 = (np.sin(val) / val for val in x) # 1st generator
    if n == 0:
        return [v for v in j0]

    j1 = ((j0val - np.cos(x[i])) / x[i] for i, j0val in enumerate(j0)) # 2nd generator
    if n == 1:
        return [v for v in j1]

    j2 = ((3 * j1val - np.sin(x[i])) / x[i] for i, j1val in enumerate(j1)) # 3rd generator

    if n == 2:
        return [v for v in j2]

    if n < 0 or n > 2:
        raise ValueError


x = np.array([0.1, 0.2, 0.3, 0.4])
print("Bessel values n = 0 : ", bessel_array(x, 2))
print("Bessel values n = 0 : ", bessel_gen(x, 2))
