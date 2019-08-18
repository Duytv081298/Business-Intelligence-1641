import numpy as np  
import math
import csv

pizza_data = []
for row in csv.reader(open("pizza_data.csv", "r"),delimiter = ','):
    pizza_data.append(row)

pizza_data = pizza_data[1:]
print(len(pizza_data))
#a,b)
clean_empty = lambda x: False if x[9] == '' or x[10] == '' or x[18] == ''or x[19] == '' else True
pizza_data = list(filter(clean_empty,pizza_data))

print(len(pizza_data))

for row in pizza_data:
    row[9] = float(row[9])
    row[10] = float(row[10])
    row[18] = float(row[18])
    row[19] = float(row[19])
    row[2] = row[2].split(",")[0]

np.savetxt("pizza.txt", pizza_data, fmt= '%s', delimiter=',',newline='\n', header='', footer='', comments='#')

print(pizza_data[-3:-1])