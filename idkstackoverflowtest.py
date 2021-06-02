import numpy as np
from scipy.interpolate import interp1d    

def NearestValue(array,value):
    #returns the index of the element of the array which is closest to value

    idx = (np.abs(array-value)).argmin()
    return idx

x =[[   0. ],[   9.9],[  19.8],[  31.5],[  41.9],[  49.1],[  59. ],[  70. ],[  80.4],[ 100. ]]

y= [ 0.011905, 0.140795, 0.600562, 0.757247, 0.874564, 0.934559, 0.961719, 0.986099,  0.990284, 0.998254]

f = interp1d(y, np.array(x).flatten())

print (f(0.95))
for i,_ in enumerate(y):
    print (_,  x[i][0], f(_))
