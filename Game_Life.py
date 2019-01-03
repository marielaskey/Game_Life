# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:38:18 2018

@author: Lauramarie
"""
#Conway's Rules:
#1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF
#2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
#3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
#4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.

import argparse 
import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

def main():
    N = 100
    updateInterval = 500
    
    #declare grid (empty grid)
    a_grid = np.array([])
    a_grid = random_grid(N)
    
    #set up animation
    fig, ax = plt.subplots()
    #to show grid at actual size (instead of fitting to screen)
    img = ax.imshow(a_grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, overwrite_grid, fargs=(img, a_grid, N, ),
        frames = 10,
        interval = updateInterval,
        save_count = 50)
    plt.show()

#values for grid
ON = 255
OFF = 0
vals = [ON, OFF]

#to generate random grid of numbers
def random_grid(N):
    #to return a grid of NxN random values; p defines 20% on, 80% off
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N,N)

#reading off a_grid, writing to new_grid simultaneously
#copy grid so all updates can run without being wiped by new updates
def overwrite_grid(frameNum, img, a_grid, N):
    new_grid = a_grid.copy()
#compute 8-neighbor sum (determine how many cells are on)
    for x in range(N):
        for y in range(N):
            total = int((a_grid[x,(y-1)%N] + a_grid[x,(y+1)%N] +
                            a_grid[(x-1)%N,y] + a_grid[(x+1)%N,y] +
                            a_grid[(x-1)%N,(y-1)%N] + a_grid[(x-1)%N,(y+1)%N] +
                            a_grid[(x+1)%N,(y-1)%N] + a_grid[(x+1)%N,(y+1)%N])/255)
            #apply Conway's rules
            if a_grid[x,y] == ON:
            #rule 1 & 2
                if (total < 2) or (total > 3):
                    new_grid[x,y] = OFF
                #rule 4
            else: #if cell is off
                if total == 3:
                    new_grid[x,y] = ON
				
#overwrite a_grid with new_grid                 
#setting image for new_grid on screen (animation)             
    img.set_data(new_grid)
#set grid
    a_grid[:] = new_grid[:]
    return img,

#call main (if in main, run main)
if __name__ == '__main__':
    main()