import numpy as np
from random import randint
import matplotlib.pyplot as plt

"""
Problem 7.2 from the Giordano book. This program will simulate a random
walk of a particle in 3D space in a way that is not bound to a grid or
mesh. 
"""
position = []
time = [0]
r2 = [0]
position.append(np.array([0,0,0]))

# contruct the unit vector for a random direction

dt = 1

for n in range(0,100):
    randX = randint(-100,100)
    randY = randint(-100,100)
    randZ = randint(-100,100)
    dS = np.array([randX,randY,randZ], float)/np.linalg.norm([randX,randY,randZ])
    position.append(position[-1] + dS)
    r2.append(np.linalg.norm(position[-1])**2)
    time.append(time[-1]+dt)

r2Avg = []
n = 1
while n < len(r2) + 1:
    avg = sum(r2[0:n])/n
    r2Avg.append(avg)
    n += 1
    
m,b = np.polyfit(time, r2Avg, 1)
print m
print b

plt.figure(1)
plt.subplot(211)
plt.scatter(time, r2Avg)
time = np.array(time)
plt.plot(time, m*time+b)
plt.show()
