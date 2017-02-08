
# coding: utf-8

# # System of 2 particles

# In[2]:

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import holoviews as hv

hv.notebook_extension('matplotlib')
get_ipython().magic('matplotlib inline')


# In[3]:

m = 1   #particle mass
n = 2   #number of particles
h = .01  #time step
L = 100 #box size
eps = 1
sigma = 0.01


# In[73]:

pos0 = np.random.rand(n,2) # one particle each row: [x y ]
print(pos0)

vel0 = np.array([[1,1],[-2,-1]]) #one particle each row: [px py]
mom0 = m*vel0
print(mom0, vel0)


# In[74]:

def newpositions(x,v):
    'calculates new positions using periodic boundary conditions'
    xnew = x + v*h
    xnew % L            #box size
    return xnew


# In[75]:

def newvelocity(x,x_nn,v):
    'returns velocity change PER PARTICLE, input: particle position x, neirest neighbour position x_nn, velocity v'
    
    r = la.norm(x-x_nn)
    unitr = (x-x_nn)/r
    
    F = -4*eps*(6*(sigma**6/r**7) - 12*(sigma**12/r**13))
    vecF = F*unitr
    
    dv = (1/m)*h*vecF
    vnew = v + dv
    
    return vnew


# In[79]:



N = 2    # #timesteps
v = vel0  #initial velocity
x = pos0  #initial velocity
XX = pos0 #position history every particle
VV = vel0 #velocity history every particle

for i in range(N):
    
    #nearest neighbour particle positions of particle 1 and 2
    x_nn = np.array([x[1,:],x[0,:]]) 
    
    #calculate new positions
    x = newpositions(x,v)
    
    #add new positions to position history matrix
    XX = np.append(XX, x, axis = 1) 
    
    for k in range(n):
        v[k,:] = newvelocity(x[k,:],x_nn[k,:],v[k,:])
    VV = np.append(VV ,v, axis = 1)



# In[81]:

print(pos0)
print(XX)
type(XX)


# In[200]:





# In[15]:

a = len(pos0)
print(a)


# In[59]:

a = np.random.rand(3,1)
print(a)
b = np.ones([3,1])
c = np.append(a,b, axis = 1)
print(b)
print(c)
d = 6*np.ones([3,2])
c = np.append(c,d, axis = 1)
c2 = c.transpose()
print(c)
print(c2)


# In[209]:

print(range(3))

