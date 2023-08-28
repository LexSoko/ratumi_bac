import numpy as np 

def F(fj,G,A_P):
    return fj*np.exp(-2j*np.pi*(np.dot(G,A_P)))

print(F(1,[1,0,0],[0.5,0.5,0]))
x = [1,0,0]
y= [0,1,0]
z = [0,0,1]

peaks = [[0,1,1],[0,0,1],[-1,0,0],[-1,-1,0]]
ag = [[0,0,0], [0,0.5,0.5],[0.5,0,0.5], [0.5,0.5,0]]
fff = []
for j in peaks:
    Ff = []
    for i in ag:
        Ff.append(F(1,j,i))
    Ff = np.array(Ff)
    print(Ff)
    fff.append( [np.sum(Ff) , j])
print(fff)