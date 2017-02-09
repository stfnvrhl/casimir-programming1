
# coding: utf-8

# # 2 Particles array tryout

# In[14]:

import numpy as np
import scipy.linalg as la


# In[15]:

L = 1
coord_particle_A = [.1,.2]
coord_particle_B = [.9,.8]
coord_particles = np.vstack((coord_particle_A,coord_particle_B))

mirror_particle_matrix = np.zeros((9,2*len(coord_particles[:,0])))

for p in range(len(coord_particles[:,0])):
        coord_particle = coord_particles[p,:]

        mirror_particle_X_coord = [coord_particle[0]-L, coord_particle[0],coord_particle[0]+L]  # L the boxlength
        mirror_particle_Y_coord = [coord_particle[1]-L, coord_particle[1],coord_particle[1]+L]

        for i in range(len(mirror_particle_X_coord)):
            for j in range(len(mirror_particle_Y_coord)):
                mirror_particle_matrix[(j)+(3*i),2*p] = mirror_particle_X_coord[i]
                mirror_particle_matrix[(j)+(3*i),2*p+1] = mirror_particle_Y_coord[j]
coord_particle_matrix =  mirror_particle_matrix               

print(coord_particle_matrix)


# In[16]:

coord_particle_matrix_A = np.zeros((9,2))
coord_particle_matrix_A = coord_particle_matrix[:,0:2]

coord_particle_matrix_B = np.zeros((9,2))
coord_particle_matrix_B = coord_particle_matrix[:,2:4]

r = np.zeros((9,1))
for q in range(len(coord_particle_matrix_B[:,0])):
    r[q,:] = la.norm(coord_particle_matrix_A[4,:]-coord_particle_matrix_B[q,:])

ind = np.argmin(r) #index of the nearest particle position
r_min = r[ind,:] # distance between the nearest particles
print(r_min)

nearest_neighbour_particle = coord_particle_matrix_B[ind,:] # coordinates of the nearest particle 
print(nearest_neighbour_particle)


# In[ ]:



