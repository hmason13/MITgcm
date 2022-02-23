# make bin for wind forcing
# cyclonic wind stress with varying strength based on radius from center
# grid size 300x300, tau max 0.1 m2s-1
# hassan mason july 8

import numpy as np
import matplotlib.pyplot as plt

hg = 150.000001

windy = np.fromfunction(lambda i,j:(i-150)/(((i-hg)**2 + (j-hg)**2)**(1/2)),
shape=(300,300))

windx = np.fromfunction(lambda i,j:(-j+150)/(((i-hg)**2 + (j-hg)**2)**(1/2)),
shape=(300,300))
 
windpower = np.fromfunction(
lambda i,j:np.sin((((i-150)**2+(j-150)**2)**(1/2))*np.pi/150), shape=(300,300))
windpower[windpower<0] = 0
windpower = 0.1 * windpower

windy = windy * windpower
windx = windx * windpower

windx.astype('>f4').tofile('windy.bin')
windy.astype('>f4').tofile('windx.bin') # SWAPPED X,Y HERE

# make bin for bathymetry
# flat bottom with 0 on boundaries for walls, 800m depth

bathymetry = np.ones(shape=(300,300))
bathymetry[[0,-1],:] = 0
bathymetry[:,[0,-1]] = 0
bathymetry = bathymetry * 800 * -1 # must be negative!

bathymetry.astype('>f4').tofile('bathymetry.bin')

# make temperature restoring profile
# I suppose for surface forcing?
# this may not be necessary as it may be turned off at some point

trest = np.fromfunction(lambda i,j: (300-i)/300, shape=(300,300))
trest = trest * 30
trest.astype('>f4').tofile('sst-relax.bin')

