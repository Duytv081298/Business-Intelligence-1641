import numpy as np
import matplotlib.pyplot as plt

# Read file vgsales.csv, columns 1, 3, 10 correspondingly
names, years, sales = np.loadtxt("vgsales.csv", usecols=(1,3,10), delimiter=',', skiprows=1,
                                 unpack=True, dtype=str)
# Zip 3 columns into a 2d list
vgsales = list(zip(names, years, sales))
# Remove rows that have names = 'N/A'
vgsales = list(filter(lambda x: False if x[1] == 'N/A' else True, vgsales))
# Sort list based on name (column 1)
vgsales = sorted(vgsales, key = lambda l: l[1])
# Ask user to enter a game name
gname = input("Enter a game name: ")
#game_sales = [list(row) for row in vgsales if gname in row[0]]
game_sales = list(filter(lambda x: True if gname in x[0] else False, vgsales))

# Extract column year
x_years = [int(row[1]) for row in game_sales]
# Extract column global
y_sales = [float(row[2]) for row in game_sales]

# Plot global sales by year for game
plt.xlabel('year')
plt.ylabel('global sales')
plt.plot(x_years, y_sales, color='r')
plt.show()
