import numpy as np
import csv

pizza_data = []

for row in csv.reader(open("pizza_data.csv","r"), delimiter=','):
    pizza_data.append(row)

# remove header row
pizza_data = pizza_data[1:]

# a,b)
clean_empty = lambda x: False if x[9] == '' or x[10] == '' \
                              or x[18] == '' or x[19] == '' else True

pizza_data = list(filter(clean_empty, pizza_data))

# convert some string columns to float
for row in pizza_data:
    row[9] = float(row[9])
    row[10] = float(row[10])
    row[18] = float(row[18])
    row[19] = float(row[19])
    row[2] = row[2].split(",")[0]  # get only 1st category in categories

#np.savetxt("pizza_data_cleaned.csv", pizza_data, fmt='%s', delimiter=',', newline='\n')
with open('pizza_data_cleaned.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    for row in pizza_data:
        writer.writerow(row)
