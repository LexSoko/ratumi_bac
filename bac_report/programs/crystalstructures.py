import numpy as np 
import matplotlib.pyplot as plt
a = 1
x = np.array([a,0,0])
y = np.array([0,a,0])
z = np.array([0,0,a])

xfcc= 1/2 * ( y+z)
yfcc = 1/2 * (z+x)
zfcc = 1/2 * (x+y)
N = 3
M = 3
K = 2
def crystallattice(N,M,K,basis):
    Origin = np.array([0,0,0])
    n = 0
    m = 0
    k = 0
    laticcepointsx = []
    laticcepointsxy = []
    laticcepointsxyz = []
    for i in range(0,N):
        currentpoint = Origin
        laticcepointsx.append(currentpoint)
        for j in basis:
            laticcepointsx.append(currentpoint + j)
        Origin = currentpoint + x
    y_trans = np.array([y]*N*4)
    z_trans = np.array([z]*N*M*4)
    print(y_trans)
    laticcepointsx =  np.array(laticcepointsx)
    for m in range(0,M):
        
        currentlatticex = laticcepointsx
        laticcepointsxy.append(currentlatticex)
        laticcepointsx = laticcepointsx  + y_trans
    laticcepointsxy_reduced = []
    for g in laticcepointsxy:
        for h in g:
            laticcepointsxy_reduced.append(h)   

    for k in range(0,K):
        currentlatticexy = laticcepointsxy_reduced
        laticcepointsxyz.append(currentlatticexy)
        laticcepointsxy_reduced = laticcepointsxy_reduced + z_trans
    laticcepointsxyz_reduced = []
    for g in laticcepointsxyz:
        for h in g:
            laticcepointsxyz_reduced.append(h)  

    

    return laticcepointsx, laticcepointsxy_reduced, laticcepointsxyz_reduced

lattice, latticexy, latticexyz = crystallattice(N,M,K,[xfcc,yfcc,zfcc])
latticexyf = []
for g in latticexy:
    for h in g:
        latticexyf.append(h)

print(latticexy, len(latticexyf))
fig  = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.axes.set_xlim3d(0,N*a)
ax.axes.set_ylim3d(0,M*a)
ax.axes.set_zlim3d(0,K*a)
for i in latticexyz:
    
    ax.scatter(i[0],i[1],i[2], marker = "o", c = "g", s = 150)
print(lattice)
plt.show()