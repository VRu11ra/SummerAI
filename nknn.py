import numpy as np
import sys

noise = float(sys.argv[1])
X = np.arange(0, 25)
Xtr = X.copy()
for i in range(0, Xtr.size):
    Xtr[i] += (Xtr[i]*(2*np.random.random()**noise)-1)

#def L2(a,b):
#    return sqrt(()**2 + ()**2)

def L2(a, b):
    return np.absolute(a-b)

# knn
n = int(sys.argv[2])


results = X[:n]
def funk():
    for k in range(0,len(results)):
        for i in range(0,X.size):
            for j in range(0,Xtr.size):
                if X[i] != 999999999:
    #                print('X= {x}, Y = {y}'.format(x= X[i], y= Xtr[j])) ##this works fine
    #                print('L2(X[i],Xtr[j]) = {a}, L2(results[k],Xtr[j]) = {b}'.format(
    #                    a = L2(X[i],Xtr[j]) , b = L2(results[k],Xtr[j])))
                    if L2(X[i],Xtr[j]) < L2(results[k],Xtr[j]):
                        results[k] = X[i]
                        X[i] = 999999999
                        funk()

print(results)
print([L2(results[i], Xtr[i]) for i in range(0,results.size)])
