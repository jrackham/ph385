import numpy as np
from random import randint
import matplotlib.pyplot as plt

"""
Problem 7.2 from the Giordano book. This program will simulate a random
walk of a particle in 3D space in a way that is not bound to a grid or
mesh. 
"""

# Generate initial conditions
position = []
time = [0]
r2 = [0]
position.append(np.array([0,0,0]))

# Do 100 random steps for the walker
dt = 1
for n in range(0,100):
    randX = randint(-100,100)
    randY = randint(-100,100)
    randZ = randint(-100,100)
    # generates a random direction unit vector
    dS = np.array([randX,randY,randZ], float)/np.linalg.norm([randX,randY,randZ])
    position.append(position[-1] + dS)
    r2.append(np.linalg.norm(position[-1])**2)
    time.append(time[-1]+dt)

# Find the average r^2 of all previous point in time. For example the average
# of the 5 time potion is found by averaging the r^2 valuse of 0-4
r2Avg = []
n = 1
while n < len(r2) + 1:
    avg = sum(r2[0:n])/n
    r2Avg.append(avg)
    n += 1

# Determing the fit function and display values    
m,b = np.polyfit(time, r2Avg, 1)
print m
print b

# Plotting
plt.figure(1)
plt.subplot(211)
plt.scatter(time, r2Avg)
time = np.array(time)
plt.plot(time, m*time+b)
plt.show()
