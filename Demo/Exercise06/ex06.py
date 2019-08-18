import numpy as np

# Create a list of 20 random integers less than 100
# Find elements that are greater than 50
# Find elements that are greater than mean of list
# Create a list of even numbers from that list
# Re-arrange the list so that 1st half contains only even numbers and 2nd half contains only odd numbers
# Create a list of even index numbers from that list, a list of odd index numbers from that list

mylist = np.random.randint(100, size=20)
print(mylist)

grt50 = [mylist[i] for i in range(20) if mylist[i] > 50]
print(grt50)

avg = np.mean(mylist)
print("mean = ", avg)

grtAvg = [mylist[i] for i in range(20) if mylist[i] > avg]
print(grtAvg)

evenList = [mylist[i] for i in range(20) if mylist[i] % 2 == 0]
print(evenList)

oddList = [mylist[i] for i in range(20) if mylist[i] % 2 != 0]
print(oddList)

mylist = evenList + oddList
print(mylist)

evenInd = [mylist[i] for i in range(0, 20, 2)]
print(evenInd)

oddInd = [mylist[i] for i in range(1, 20, 2)]
print(oddInd)
