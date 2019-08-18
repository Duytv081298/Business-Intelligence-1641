# Create a list of 20 integers
#   a) Slice 1st half and 2nd half of the list
#   b) Slice list to get a sublist that removes n elements at begin and n elements at end of list (n from keyboard)
#   c) With n from keyboard, get n first elements and n last elements, join them to make a new list of 2n elements
#   d) With n from keyboard, get nth element from list. What happen if n is out of index range?

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lHalf = int(len(a) / 2)

print("a) 1st way: ", a[:10])
print("a) 2nd way: ", a[:lHalf])
print("a) 3rd way: ", a[:-10])

n = int(input("Enter n: "))

print("b) ", a[n:-n])

c = a[:n] + a[-n:]

print("c) ", c)

print("a[{0}] = {1}".format(n, a[n]))
