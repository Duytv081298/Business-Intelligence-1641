import numpy as np

# a) Create an 8 × 8 array with ones on all the edges and zeros everywhere else.
a = np.ones((8, 8))
a[1:-1, 1:-1] = 0

print("a) ", a)

print()
# b) Create an 8 × 8 array of integers with a checkerboard pattern of ones and zeros.

b = np.ones((8, 8))
b[0::2, 1::2] = 0
b[1::2, 0::2] = 0

print("b) 1st way: ", b)

print()

r1 = [1, 0, 1, 0, 1, 0, 1, 0]
r2 = [0, 1, 0, 1, 0, 1, 0, 1]
b  = [r1, r2, r1, r2, r1, r2, r1, r2]
b  = np.reshape(b, (8, 8))

print("b) 2nd way: ", b)



# c) Create an 8 x 8 array of random integers, make all the numbers not divisible by 3 negative.
c = np.random.randint(low=0, high=100, size=(8, 8))
c[c%3 != 0] *= -1

print("c) ", c)

# d) Split the matrix above into 4 submatrices 4x4
q1 = c[0:4, 0:4]
q2 = c[0:4, 4:]
q3 = c[4:, 0:4]
q4 = c[4:, 4:]

print('q1 = {0}, size = {1}, shape = {2}, mean = {3}, std = {4}'.format(
      q1, q1.size, q1.shape, np.mean(q1), np.std(q1)))
print("q2 = ", q2)
print("q3 = ", q3)
print("q4 = ", q4)
