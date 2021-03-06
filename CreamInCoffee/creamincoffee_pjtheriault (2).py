#!/usr/bin/env python
# coding: utf-8

# In[38]:


#Written by Paul Theriault
#The purpose of this program is to simulate diffusion

#Problem 1
import math
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random
get_ipython().run_line_magic('matplotlib', 'inline')

#We want a grid 201 by 201 with 100 particles at origin and we want time to evolve to distribute the particles
Ngrid = 200
Nparticles = 400
Nsteps = 2000000
plot=1000000
X = np.zeros(Nparticles)
Y = np.zeros(Nparticles)
X = [Ngrid/2]*Nparticles
Y = [Ngrid/2]*Nparticles
#particle
for i in range(Nsteps):
    #choose a particle 
    p_index = random.randint(Nparticles)
    #print(p_index) 
    #picks a random direction
    direction = random.randint(4)
    #0 left, 1 right, 2 up, 3 down the and part keeps the particles inside the grid
    if direction == 0 and X[p_index] >= -Ngrid:
        X[p_index] -=1 
    if direction == 1 and X[p_index] <= Ngrid:
        X[p_index] +=1
    if direction == 2 and Y[p_index] <= Ngrid:
        Y[p_index] +=1
    if direction == 3 and Y[p_index] >= -Ngrid:
        Y[p_index ] -=1
    if (i + 1) % int(plot) == 0:
        plt.figure()
        plt.title('Cream in Coffee: Steps = %.2E' %(i + 1))
        plt.plot(X, Y, '.')
        plt.xlabel('Length')
        plt.ylabel('Length')
        plt.xlim(0, Ngrid)
        plt.ylim(0, Ngrid)
        
#################################################################################################################################

#Problem II: Hole in a box

Ngrid = 200
Nparticles = 400
Nsteps = 2000000
gap = 40

X = [Ngrid/2]*Nparticles
Y = [Ngrid/2]*Nparticles
Plist=[]
Nlist=[]
Ncurrent = Nparticles
for i in range(int(Nsteps)):
    #choose a particle 
    p_index = random.randint(Nparticles)
    #print(p_index) 
    #picks a random direction
    direction = random.randint(4)
    #0 left, 1 right, 2 up, 3 down the and part keeps the particles inside the grid
    if direction == 0 and X[p_index] >= -Ngrid:
        X[p_index] -=1 
    if direction == 1 and X[p_index] <= Ngrid:
        X[p_index] +=1
    if direction == 2 and Y[p_index] <= Ngrid:
        Y[p_index] +=1
    if direction == 3 and Y[p_index] >= -Ngrid:
        Y[p_index ] -=1
    if X[p_index] == 0 and (Ngrid-gap)/2 <= Y[p_index] <= (Ngrid+gap)/2:
        z = str('a particle has left the box')
        Plist.append(z)
    if X[p_index] == 0 and (Ngrid-gap)/2 <= Y[p_index] <= (Ngrid+gap)/2:
        X[p_index] = 1000000
        Ncurrent -= 1
    Nlist.append(Ncurrent)

print(len(Plist), 'particles have left the box'), print(Nparticles-len(Plist), 'remain inside')
#plt.figure()
#plt.title('Hole in the Box 1')
#plt.plot(range(int(Nsteps + 1)), Nlist, 'r')
#plt.xlabel('Number of Steps')
#plt.ylabel('Number of Particles in Box')

#I was having problems graphing this so I decided to exlcude it. However I did determine a way to show how many particles left
#the box using a list and the len of that list.
#The graph should show that larger step sizes are correlated to more particles leaving the box.
#You can check this by increasing the size of Nsteps and comparing. 

#Final comments: The diffusion worked out as expected. The hole in the box works as expected as well. My graph was giving me
#problems however.


# In[ ]:




