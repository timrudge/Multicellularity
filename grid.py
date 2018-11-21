import numpy as np
import scipy as sp
from scipy.ndimage.filters import laplace
import random
import matplotlib
import matplotlib.pyplot as plt

nx = 10
ny = 10
nt = 100
initcells = 2

kd = 0.1
pgrow = 0.1

cellgrid = np.zeros((nx,ny,nt))
signalgrid = np.zeros((nx,ny,nt))

def initgrid(n):
    # Initialise cells in the grid
    for i in range(n):
        x = int(random.uniform(0,nx))
        y = int(random.uniform(0,ny))
        cellgrid[x,y,0] = 1
        
    plt.figure()
    plt.imshow(cellgrid[:,:,0]) 

def grow(x,y,p):
    throw = random.uniform(0,1)
    if throw<p:
        # Choose random neighbour
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        nb = random.randint(0,4)
        cellgrid[x+dx[idx], y+dy[idx]
        
def main():
    initgrid(initcells)
    # Loop over time
    for t in range(nt):
        x,y = np.where(cellgrid[:,:,0])
        print(x,y)
        for i in range(len(x)):
            xx = x[i]
            yy = y[i]
            signalgrid[xx+1,yy,1] += 1

            
        signalgrid = signalgrid + laplace(signalgrid)*kd
    
    plt.figure()
    plt.imshow(signalgrid[:,:,0]) 
