# hassan mason
# nov 2021
# generate hydrogThetaFile

import numpy as np

multiplier = np.linspace(10,9.75,50)
domain = np.ones(shape=(400,400,50))
i_temp = domain * multiplier
i_temp.astype('>f4').tofile('Theta_initial_nf5.bin')
