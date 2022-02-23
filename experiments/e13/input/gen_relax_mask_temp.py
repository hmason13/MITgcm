# hassan mason nov 2021
# gen relax mask file

import numpy as np

# create 3d mask file, 1 on boundaries
mask = np.zeros(shape=(398,398,50))
mask = np.pad(mask,((1,1),(1,1),(0,0)),'constant',constant_values=1)
mask.astype('>f4').tofile('T_relax_mask.bin')

# create temp relax file
# this time pray it relaxes correctly
# double loop to ensure correct behavior
profile = np.linspace(10,9.25,50)
temp_relax = np.zeros(shape=(400,400,50))
for idex in range(400):
	for jdex in range(400):
		temp_relax[idex,jdex,:] = profile[:]
temp_relax.astype('>f4').tofile('temp_relax.bin')
