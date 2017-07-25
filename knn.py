import numpy as np
from random import random
from math import sqrt
# import pandas as pd
'''
Tr = np.array([[time, amp, dist, label],...])
Re = np.array([[time, amp, dist, label],...])
'''
def func(size, hard, maxInterference, period, low, high):
    a = np.arange(1, size)
    iter = 0
    out = np.zeros(size-1)
    for i in a:
        if(high>= iter and iter >=low):		
            out[iter] = np.sin(i*(2*np.pi)/period)
        else:
            out[iter] = 0
        if (hard is not True):
            for alpha in np.random.rand(maxInterference):
                out[iter] += random.random()*np.sin(((i*np.pi*2)/period)+alpha) #generate interference
        iter +=1
    return np.asarray(out)

# print(func(200,'y',0,100,0,200))


class KNN:

    Tr, Re = np.array([]), np.array([])
    k = 0

    def __init__(self, tr, re, K):
        global Tr, Re, k
        Tr = tr, Re = re
        # set all the data that we'll need as global fields
        k = K  # hyperparameter
    '''
    get nearest k neighbors and check if they're of type hard or soft.
    Majority rules, might need something to compensate for offset.
    returns predictions
    '''


    def label(self):
        for i in Re:  # for every input
            for j in range(0, Tr.size):
                # for each point, check distance, used by index so that it was 
                # by pointer
                Tr[j[2]] = sqrt((Tr[j[0]]-i[0])**2 + (Tr[j[1]]-i[1])**2)
                # L2 Euclidian
            # need to check here if j was referenced by pointer or by copy
            Tr = np.sort(Tr, axis = 2)
            print(Tr)
            # need to check here that right axis was targeted and no data was lost
            print(Tr)
            # count up each of type here and return that as tag
            hard = 0
            soft = 0
            for l in range(0, k):
                if Tr[3] is True:
                    hard += 1
                elif Tr[3] is False:
                    soft += 1
                else:
                    raise Exception("datatype was not bool in Tr[3] this should never happen")
            if hard >= soft:
                i[3] = True
            else:
                i[3] = False
        return Re

Knn = KNN(func(200, 'y', 0, 100, 0, 200), func(10, 'y', 0, 5, 0, 10), 1)
print(Knn.label())
