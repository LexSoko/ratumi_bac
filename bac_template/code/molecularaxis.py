import uncertainties as un
from uncertainties import umath
import numpy as np

def winkel(G,A):
    return umath.atan(G/A)


G_Ag = un.ufloat(1,0.1)
A_Ag = un.ufloat(8.1,0.1)

G_MgO = un.ufloat(0.2,0.1)
A_MgO = un.ufloat(4.2,0.1)

G_sil = un.ufloat(0.5,0.1)
A_sil = un.ufloat(6.2,0.1)
print("axis silver:", (winkel(G_sil,A_sil)/(2*np.pi))*360 )
print("molecularaxis Ag:", (winkel(G_sil,A_sil)/(2*np.pi))*360 + (winkel(G_Ag,A_Ag)/(2*np.pi))*360)
print("molecularaxis MgO:", (winkel(G_sil,A_sil)/(2*np.pi))*360 - (winkel(G_MgO,A_MgO)/(2*np.pi))*360)