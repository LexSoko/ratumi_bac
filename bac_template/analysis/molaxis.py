import numpy as np 
import uncertainties as un 

def angle(x,y):
    return np.arctan(x/y)


a = un.ufloat()