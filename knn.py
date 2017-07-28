import numpy as np
import pandas as pd
import pylab as pl
import random
from math import sqrt
import sys
import argparse


parser = argparse.ArgumentParser(description="knn")
parser.add_argument("-d", action="store_true")
parser.add_argument("-Re", action="store_true")

# if vars(parser.parse_args(["-Re"])).get("Re") == True:
#     pass # todo link to main()
# elif vars(parser.parse_args(["-Re"])).get("Re") == False:
#     pass # todo also link to main
# else:
#     raise Exception
#
#
# # displays via pandas
# if vars(parser.parse_args(["-d"])).get("d") == True:
#     pass # todo link to main()
# elif vars(parser.parse_args(["-d"])).get("d") == False:
#     pass # todo also link to main
# else:
#     raise Exception


def gen(size, hard, max_interference, period, low, high):
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
        if high >= iter and iter >= low:
            out[iter] = np.sin(i*(2*np.pi)/period)
        else:
            out[iter] = 0
        if hard is not True:
            for alpha in np.random.rand(max_interference):
                out[iter] += random.random()*np.sin(((i*np.pi*2)/period)+alpha) # generate interference
        iter += 1
    out = np.asarray(out)
    out = np.reshape(out, (out.size, 1))
    out = np.pad(out, ((0, 0), (0, 1)), mode='constant', constant_values=0)
    out = np.asarray(out)
    tile = np.expand_dims(np.tile(hard, out.shape[0]), axis=1)
    out = np.concatenate((out, tile), axis=1)
    arange = np.expand_dims(np.arange(0,out.shape[0]), axis=1)
    out = np.concatenate((out, arange), axis=1)
    return out # returns proper try out[:,0]


def Tr(size, max_interference, period, low, high, num):
    out = gen(size, 'y', max_interference, period, low, high)
    for i in range(0, num):
        if int(random.random()*2) == 1:
            alpha = gen(size, 'y', max_interference, period, low, high)
            out = np.concatenate((out, alpha),axis=0)
        else:
            out = np.concatenate((out, gen(size, 'n', max_interference, period, low, high)),axis=0)
    return out
# print Tr(size=10, max_interference=0, period=5, low=0, high=10, num=5)
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
            # L2 Euclidian, where the magic happens
        Tr = np.sort(Tr, axis = 0)
        # need to check here that right axis was targeted and no data was lost
        # count up each of type here and return that as tag
        # print Tr todo should work here?, I'm seeing the 1 tags
        hard = 0
        soft = 0
        print Tr
        for l in range(0, k):
            print Tr[l][2]
            if Tr[l][2] == 1.0:
                hard += 1
                print "hard"
            elif Tr[l][2] == 0.0:
                soft += 1
            else:
                raise Exception("datatype was not bool in Tr[3] this should never happen")
        if hard >= soft:
            Re[i][2] = 1.0
        else:
            Re[i][2] = 0.0
    Ohard = 0
    Osoft = 0
    for lab in Re:
        if lab[2] == 1.0:
           Ohard +=1
        else:
           Osoft +=1

    print Ohard
    print Osoft
    if soft >= hard:
        return "soft"
    else:
        return "hard"
Training = Tr(size=200, max_interference=5, period=5, low=0, high=200, num=100)
Real = gen(size=100, hard='n', max_interference=5, period=5, low=0, high=100)
pl.plot(Real[:,0])
pl.show()
pl.plot(Training[:,0])
pl.show()

res = label(Training, Real, k=90, weight=.001)
#print res
 # def main():
 #     b, c = np.hsplit(df,2)
 #     I = [b, c]
 #     b, c = (np.asarray(v).flatten() for v in I)
 #     pl.plot(b,c)
 #     pl.show()

