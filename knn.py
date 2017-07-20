import numpy as np
import sqrt
import pandas as pd
'''
Tr = np.array([[time, amp, dist, label],...])
Re = np.array([[time, amp, dist, label],...])
'''

class KNN:
    def __init__(Tr, Re, k):
        # set all the data that we'll need as global fields
        self.Tr = Tr, self.Re = Re
        self.k = k  # hyperparameter
    '''
    get nearest k neighbors and check if they're of type hard or soft.
    Majority rules, might need something to compensate for offset.
    returns predictions
    '''
    def label():
        for i in self.Re:  # for every input
            for j in range(0,self.Tr.size): # for each point, check distance, used by index so that it was by pointer
                self.Tr[j[2]] = sqrt((self.Tr[j[0]]-i[0])**2 + (self.Tr[j[1]]-i[1])**2)  # L2 Euclidian
            # need to check here if j was referenced by pointer or by copy
            self.Tr = np.sort(self.Tr, axis = 2)
            # need to check here that right axis was targeted and no data was lost
            print(self.Tr)
            # count up each of type here and return that as tag
            hard = 0
            soft = 0
            for l in range(0, self.k):
                if self.Tr[3] is True:
                    hard += 1
                elif self.Tr[3] is False:
                    soft += 1
                else:
                    raise Exception("datatype was not bool in self.Tr[3] this should never happen")
            if hard >= soft:
                i[3] = True
            else:
                i[3] = False
        return self.Re
