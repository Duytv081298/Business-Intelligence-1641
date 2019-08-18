import numpy as np

def fibonacci_gen():
    a = 0
    b = 1
    while True:
        yield a
        c = a
        a = b
        b += c
def fibonacci(n):
    i = -1 
    for fib in fibonacci_gen():
        i +=1
        if i == n:
            return fib
for n in range(10):
    print(fibonacci(n), end=" ")

a = np.array([["john", "10:05", 4],
              ["paul", "10:35", 5],
              ["ringo", "10:00", 3],
              ["george", "12:01", 6]])   
npizzas = (row[2] for row in a)
sold = (12.5*int(n) for n in npizzas)
sum_sold = sum(sold)
print("\n",sum_sold)
print(type(sold))

# Write a function that generate an odd number (giving n => 2n+1) 
# by using generator with the formula: an = an-1 + 2 (a0 = 1)

def odd_number():
    a = 1                   #a0 = 1
    while True:
        yield a
        a = a + 2           # an = a(a-1) +2

def get_n_generator(n, generator):
    i = 0
    for it in generator():
        if i == n:
            return it
        i += 1
print("Odd {0} th: {1}".format(5,get_n_generator(5, odd_number)))
    
def pyramial_gen():
    i = 0 
    pyn = 0                     #pyn(0) = 0
    while True:
        yield pyn
        i += 1
        pyn = pyn + i**2        #pyn(n) = pyn(n-1) + n^2

print("pyramial {0} th: {1}".format(5,get_n_generator(5, pyramial_gen)))