import numpy as np

# 1. Create array of 10 integers from 0 to 20 (exclusive), equally spacing by using linspace
# 2. Create array of 10 integers from 0 to 20 (exclusive), equally spacing by using arange
# 3. When should we use linspace vs arange?
# 4. Create array of 20 random integers (max 99)
#     https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randint.html
# 5. Get sub-array from that, contains only even numbers, sort them ascending
# 6. Re-arrange array created from a) so that 1st half contains only even numbers, 2nd half contains only odd numbers (hint: use concatenate function of numpy), each half is sorted


a = np.linspace(0, 20, 10, dtype=int, endpoint=False)
print("1. ", a)

b = np.arange(0, 20, 2, dtype=int)
print("2. ", b)

c = np.random.randint(100, size=20)
print("4. ", c)

evenc = c[c%2 == 0]

print("5. ", sorted(evenc))

oddc = c[c%2 != 0]

c = np.concatenate([evenc, oddc])

print("6. ", c)

#################
y = np.array([0., 1.3, 5. , 10.9, 18.9, 28.7, 40.])
t = np.array([0., 0.49, 1. , 1.5 , 2.08, 2.55, 3.2])

v = (y[1:] - y[:-1])/(t[1:] - t[:-1])

np.set_printoptions(precision=2)
print("y = ", y)
print("t = ", t)
print("Velocity: ", v)

#################
names = np.array(['john', 'paul', '', '', 'ringo', '', 'george harrison'])
ages = np.array([20, 30, -10, 155, 120, 39])

names[names == ''] = "John Doe"
print(names)

ages[ages < 0] = 0
ages[ages > 150] = 150

print(ages)

print("Longest name  = ", max(names, key=len))
print("Shortest name = ", min(names, key=len))

print("Longest name size  = ", max(list(map(len, names))))
print("Shortest name size = ", min(list(map(len, names))))
