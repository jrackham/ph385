"""
This program will model the wave equation of a guitar string. It will take
into account stiffness following the method describe in the Giordano text

Physical Parameters:
L = 650 mm

Tension, diameter info:
D'addario EJ27N

"""
import numpy as np
import matplotlib as plt

L = 0.650 # meters
T = 66.856 # Newtons
linMass = 1 # Linear mass density
eps = 1 # Stiffness parameter

dx = L/650
dt = 0.05
v = np.sqrt(T / linMass)
r = v * dx / dt
N = L/dx

x = np.linspace(0, 0.650, dx, True)
print (x)
initialCon = []

for i in x:
    if x < 0.350:
        print "Check"
        initalCon.append(0.01 / 350.0 * x)
    else:
        print "Check2"
        initialCon.append(-0.01 / 300.0 * x)

# Ensuring boundary conditions
#initialCon[0] = 0
#initialCon[-1] = 0


yPrev = initialCon
yCurrent = initialCon
sample = []
 
for n in range(0,10):
    for i in range(0,len(x)):
        if i !=0 and i != 649:
           yNew = ((2 - 2*r**2 - 6 * eps * r**2 * N**2)*yCurrent[i] 
                   - yPrev[i] + r**2*(1 + 4*eps*N**2)*(yCurrent[i+1] 
                    + yCurrent[i-1]) - eps*r**2*N**2 *(yCurrent[i+2] 
                    + yCurrent[i-2]))
                   
        yPrev = copy(yCurrent)
        yCurrent = copy(yNew)
        plt.scatter(yNew)
        plt.draw()
        plt.pause()
        plt.clf()
                    
                   
                   
        
    
