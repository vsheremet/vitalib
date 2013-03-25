import numpy as np

def nearxy(x,y,xp,yp):
    """
    i,min_dist=nearxy(x,y,xp,yp)
    
    find the closest node in the array (x,y) to a point (xp,yp)
    
    input:
        x,y - np.arrays of the grid nodes, cartesian coordinates
        xp,yp - point on a plane
    output:
        i - index of the closest node
        min_dist - the distance to the closest node
    
    For coordinates on a sphere use function nearlonlat

    Vitalii Sheremet, FATE Project         
    """
    dx=x-xp
    dy=y-yp
    dist2=dx*dx+dy*dy  
#    dist1=np.abs(dx)+np.abs(dy)  
    i=np.argmin(dist2)
    min_dist=np.sqrt(dist2[i])  
    return i,min_dist

def nearlonlat(lon,lat,lonp,latp):
    """
    i,min_dist=nearlonlat(lon,lat,lonp,latp)
    
    find the closest node in the array (lon,lat) to a point (lonp,latp)
    
    input:
        lon,lat - np.arrays of the grid nodes, spherical coordinates, degrees
        lonp,latp - point on a sphere
    output:
        i - index of the closest node
        min_dist - the distance to the closest node, degrees
    
    For coordinates on a plane use function nearxy

    Vitalii Sheremet, FATE Project         
    """
    cp=np.cos(latp*np.pi/180.)
# approximation for small distance
    dx=(lon-lonp)*cp
    dy=lat-latp
    dist2=dx*dx+dy*dy  
#    dist1=np.abs(dx)+np.abs(dy)  
    i=np.argmin(dist2)
    min_dist=np.sqrt(dist2[i])  
    return i,min_dist 
