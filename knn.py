import numpy as np
from random import random
from math import sqrt
# import pandas as pd


def func(size, hard, maxInterference, period, low, high):
    if hard == 'y':
        hard = True
    elif hard == 'n':
        hard = False
    else:
        raise Exception

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
    out = np.asarray(out)
    out = np.reshape(out, (out.size, 1))
    out = np.pad(out,((0,0),(0,1)), mode= 'constant', constant_values= 0)
    out = np.asarray(out)
    #test below
    tile = np.expand_dims(np.tile(hard, out.shape[0]), axis=1)
    out = np.concatenate((out, tile), axis=1)
    arange = np.expand_dims(np.arange(0,out.shape[0]), axis=1)
    out = np.concatenate((out, arange), axis=1)
    return out


'''
 get nearest k neighbors and check if they're of type hard or soft.
 Majority rules, might need something to compensate for offset.
 returns predictions
 '''
'''
Tr = np.array([[amp, dist, label, time],...])
Re = np.array([[amp, dist, label, time],...])
'''


def label(Tr, Re, k, weight):
    for i in range(0, Re.shape[0]):  # for every input
        for j in range(0, Tr.shape[0]):
            # for each point, check distance, used by index so that it was
            # by pointer
            Tr[j][1] = sqrt((float(Tr[j][0])-float(Re[i][0]))**2
                            + (weight*(float(Tr[j][3])-float(Re[i][3])))**2)
            # L2 Euclidian
        Tr = np.sort(Tr, axis = 0)
        # need to check here that right axis was targeted and no data was lost
        # count up each of type here and return that as tag
        hard = 0
        soft = 0
        print Tr[1][2]
        for l in range(0, k):
            if Tr[l][2] == 1.0:
                hard += 1
            elif Tr[l][2] == 0.0:
                soft += 1
            else:
                raise Exception("datatype was not bool in Tr[3] this should never happen")
        if hard >= soft:
            Re[i][2] = 1.0
        else:
            Re[i][2] = 0.0
    return Re

Re = label(func(10, 'n', 0, 5, 0, 10), func(200, 'n', 0, 100, 0, 200), 1, 1)
print Re
