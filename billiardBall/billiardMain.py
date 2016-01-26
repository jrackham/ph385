"""
This is the main function that will handle the movement of a billiard ball
within a specified stadium. The stadium that will be examined is an elongated
circle that where the total elongation is equal to 2*alpha*radius
"""
import numpy as np

# this function will check to see if position parameters lie outside of the
# stadium. Returns a boolean value. True if position is within the stadium
# and false if the position is outside.
def insideStadium(x,y, alpha, radius):
    if (abs(x) < radius and (abs(y) < (np.sqrt(radius**2 - x**2) + alpha * radius))):
        return True
    else:
        return False
    
# Takes and input position that lies within the stadium and returns
# the point where the ball collides with the stadium.
def collisionPoint(x, y, vlist, dt):
    xlist = [x]
    ylist = [y]
    t = [0]
    while (insideStadium):
       points = eulersStep(x, y, vlist, dt/10)
       xlist.append(points[0])
       ylist.append(points[1])
       t.append(t[-1] + points[2])
    return [x[-1],y[-1],t[-1]]    

# Calculates the normal vector at a given boundary point
def normal(x,y,alpha,radius):
    posVec = np.array([x,y])
    
    if y > alpha*radius:
        radVec = np.array([0,alpha*radius])
    elif y< -alpha*radius:
        radVec = np.array([0,-alpha*radius])
    elif (abs(y) >= alpha * radius and x < 0):
        radVec = np.array([-1,0])
    else:
        radVec = np.array([1,0])
    
    result = np.array([0,0])        
    if abs(y) < alpha * radius:
        result = radVec
    else:
        result = radVec - posVec
    
    return result/np.linalg.norm(result)
        
# takes in the velocity before collision, the collision point and then returns
# the velocity after collision which the initial velocity relfect about the
# normal at collision point
def reflectVel(v, x, y):
    return true

# This function will take x and y values and iterate a single
# Euler's method step
def eulersStep(x, y, vlist, dt):    
    x = x + v[0]*dt
    y = y + v[1]*dt

    return [x, y, dt]
    
#this will generate the x, y, and time lists for a given value of alpha
def runTrial(x0, y0, v0List, tMax, alpha, radius):
    x = [x0]
    y = [y0]
    v = v0list
    time = [0]
    
    while (time[-1] < tMax):
        if (insideStadium(x[-1], y[-1], alpha, radius)):
            pts = eulersStep(x[-1], y[-1], v, dt)
            x.append(pts[0])
            y.append(pts[1])
            time.append(time[-1] + pts[2])
        else:
            intersect = collisionPoint(x[-1],y[-1],velocity,dt)
            x.append(intersect[0])
            y.append(intersect[1])
            time.append(time[-1]+intersect[2])
            #calculate norm
            #relfect and update velocity

# Generates the Lyanpunof chart and exponent for a given alpha calculate the
# the distance between two endpoints of trial after the specified time interval
#   


print(insideStadium(-0.5,0.5,1,1))
print(normal(-1,1,1,1))