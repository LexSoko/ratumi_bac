import numpy as np 
import matplotlib.pyplot as plt
from tqdm import tqdm
import numba as nb 
def mandel(Re,Im, max_Iter):
    c = complex(Re,Im)
    z = 0.0j
    for i in range(0,max_Iter):
        z = z*z + c
        if((z.real)**2 + (z.imag)**2) >= 10:
            return i
    return max_Iter

def sokomenge(Re,Im,max_Iter, pot):
    c = complex(Re,Im)
    z = 0.0j
    for i in range(0,max_Iter):
        z = z**pot + c
        if ((z.real)**2 + (z.imag)**2) >=2:
            return i 
    return max_Iter
coloums = 10000
rows = 10000

A = np.zeros((rows,coloums))
for row_index, Re, in tqdm(enumerate(np.linspace(-2,1,num=rows)), desc= "row_loop"):
    for coloum_index, Im in enumerate(np.linspace(-1,1, num = coloums)):
        A[row_index,coloum_index] = sokomenge(Re,Im,100,4.2)

plt.matshow(A)
plt.show()