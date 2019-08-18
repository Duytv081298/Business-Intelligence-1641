# Create a 5 x 5 list of floating numbers
#   a) Get 3 middle rows in as many ways as you can
#   b) Get 2 last rows in as many ways as you can
#   c) Enter n from keyboard, get max, min of nth row and print them with 2 digits after the point (hint: using function max, min)
#   d) Enter n from keyboard, get sum of nth row and print it with 4 digits after the point (hint: using function sum)
#   e) Enter n from keyboard, sort nth row and print it (hint: using function sorted)

a = [[1., 2., -3.3, -10.5, 5.],
     [2., 55.3, 34., -8., 9.9],
     [3., 33., 44., 55., 66.],
     [4., 32., 20.4, -45., 0.],
     [5., 32, 55, 12.3, 30.]]

print(a)

print("a) 1st way: ", a[1:4])
print("a) 2nd way: ", a[1:-1])

print("b) 1st way: ", a[3:5])
print("b) 2nd way: ", a[3:])
print("b) 3rd way: ", a[-2:])
print("b) 4th way: ", a[-2:5])

n = int(input("Enter n: "))

print("c) Max of row {0} = {1:0.2f}".format(n, max(a[n])))
print("c) Min of row {0} = {1:0.2f}".format(n, min(a[n])))
print("d) Sum of row {0} = {1:0.4f}".format(n, sum(a[n])))

print("e) Row {0} is sorted: ".format(n), sorted(a[n]))
