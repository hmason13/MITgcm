# hassan Oct 2021
# script that generates the correct surface forcing
# adapted from genmake file in MITgcm tutorial docs

import numpy as np

# grid dimensions
nx=400
ny=400
nz=50
H = -1000 

# Size of domain
Lx = 20000

# Radius of cooling disc
Rc = 2000

# horizontal resolution
dx = Lx/nx

# rotation
f=1e-4

#stratification
N=0 #not true but let's role with it

# surface temperature
Ts = 20

#gravity
g = 9.81

# define the Q grid
Q = np.ones(shape=(400,400))
Discmaker = np.fromfunction(lambda i,j:(i-200)**2+(j-200)**2 < 50**2 ,(400,400))
Discmaker = Discmaker.astype(int)
Q[Discmaker==0] = 0
Q = Q*800
Q.astype('>f4').tofile('Qsurface-custom.bin')

