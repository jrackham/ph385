#This is problem 4.5 from the Giordano text. The purpose of this problem is
#plot the orbit of some planetoid around the sun and then find out whether
#or not the various forms of energy are conserved. There will be multiple
#functions presented to accomplish this purpose.
import matplotlib.pyplot as plt
from numpy import array, cross
from math import pi
from numpy.linalg import norm


#This function serves the purpose of implementing the Runga Kutta method, it
#will take in some variables from the getArrays function and then return
#those to the aforementioned function.
def getDerivs(things):
    G = 4
    Ms = pi**2
    x = things[0]
    y = things[1]
    vx = things[2]
    vy = things[3]
    r = array([x,y],float)
    dx = vx
    dy = vy
#This norm function takes an array and returns the magnitude of that array
#note that in order to actually use this you have to be able to have your 
#array listed as a numpy array or else it will not know what to do
    dvx = -(G*Ms*x)/(norm(r)**3)
    dvy = -(G*Ms*y)/(norm(r)**3)
    return array([dx,dy,dvx,dvy], float)

#This function serves the purpose of ensuring that all of the arrays are
#generated in such a way as to ensure easy editing and then to return those
#to the plot_it_all function.
def getArrays(arrays):
    x = [arrays[0]]
    y = [arrays[1]]
    vx = [arrays[2]]
    vy = [arrays[3]]
    t = [0]
    dt = .01
    while t[-1] < 1.5:
        k1 = dt * getDerivs(arrays)
        k2 = dt * getDerivs(arrays + 0.5*k1)
        k3 = dt * getDerivs(arrays + 0.5*k2)
        k4 = dt * getDerivs(arrays + k3)
        arrays = arrays + (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)
        x.append(arrays[0])
        y.append(arrays[1])
        vx.append(arrays[2])
        vy.append(arrays[3])
        t.append(t[-1] + dt)
    return x,y,vx,vy,t

#This function is used to calculate the Kinetic and Potential Energies of
#the system. It does this by doing the simple step by step calculations
#for the system.
def energy(pieces):
    K = []
    P = []
    T = []
    l = []
    for i,k in enumerate(pieces[4]):
        v = array([pieces[2][i],pieces[3][i]], float)
        r = array([pieces[0][i],pieces[1][i]], float)
        L = cross(r,v) #array([v[0]*r[1],-v[1]*r[0]], float)
        K.append(0.5*norm(v)**2)
        P.append(-(4.*(pi**2))/norm(r))
        T.append(0.5*norm(v)**2-((4.*(pi**2))/norm(r)))
        l.append(norm(L))
    return K,P,T,l

#This function starts the program and then retrieves the lists from all of
#the other functions to then in turn plot it for us to see what occurred
#within the program.
def plot_it_all(initial_conditions):
    x,y,vx,vy,t = getArrays(initial_conditions)
    k,p,T,l = energy([x,y,vx,vy,t])
    plt.close('all')
    plt.plot(t,k,'g--',t,p,'r--',t,T,'y--',t,l,'b--')
    plt.title('Green for K, R for P, Y for T, L is black')
    plt.show()
'''    plt.figure(1)
    plt.subplot(221)
    plt.xlabel('X Displacement (AU)')
    plt.ylabel('Y Displacement (AU)')
    plt.title('Orbit of some Planet about Sun')
    plt.scatter(x,y)
    plt.subplot(222)
    plt.xlabel('Time (yr)')
    plt.ylabel('Energy')
    plt.title('Energy during the whole time of Simulation')
    plt.scatter(t,k,t,p)
    plt.subplot(223)
    plt.xlabel('Time(yr)')
    plt.ylabel('Total Energy')
    plt.title('Total Energy over Time')
    plt.scatter(t,T)
    plt.subplot(224)
    plt.xlabel('Time(yr)')
    plt.ylabel('Angular Momentum')
    plt.title('Angular Momentum with Time')
    plt.scatter(t,l)'''

#These are the conditions to use as specified in the text
conditions0 = array([1.,0.,0.,5.], float)
plot_it_all(conditions0)
