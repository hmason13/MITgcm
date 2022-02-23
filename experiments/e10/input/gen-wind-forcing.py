#hassan mason
#generate merid wind file e10 e9

import numpy as np

wind = np.ones(shape=(400,400))
Discmaker = np.fromfunction(lambda i,j:(i-200)**2+(j-200)**2 < 50**2 ,(400,400))
Discmaker = Discmaker.astype(int)
wind[Discmaker==0] = 0
wind = wind*0.1 #corresponds to wind velocity of 10 m/s on disc
wind.astype('>f4').tofile('merid_wind_forcing.bin')