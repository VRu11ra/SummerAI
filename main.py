import numpy as np
import random
import pandas as pd
import sys

'''
How to call:
    python main.py size hard(y/n) interference period
size: sample number of points to plot
hard: gen interference?
interference: how much to garble signal
period: how many cycles to display
interference appears to work counterintuitively, where as interference value increases, the actual variance decreases. This isn't an immediate issue and can be ignored. 

'''


class DataSet:
  data = np.array([[],[]]) #[time],[amp]
  time = 0
  def __init__(self,amps):
    time = amps.shape
    data = np.array([[np.arange(1,time)],amps])

#random data generation, generates amplitudes
def func(size, hard, maxInterference,period):
  a = np.arange(1,size)
  iter = 0
  out = np.zeros(size-1)
  for i in a:
    out[iter] = np.sin(i*(2*np.pi)/period)
    if (hard != True):
      for alpha in np.random.rand(maxInterference):
        out[iter] += random.random()*np.sin(((i*np.pi*2)/period)+alpha) #generate interference
    iter +=1
  return out


#print(func(200,True,3,2))

#cli interface
if(sys.argv[2] == 'y'):
    set1Test = func(int(sys.argv[1]),True,int(sys.argv[3]),int(sys.argv[4]))
elif(sys.argv[2] == 'n'):
    set1Test = func(int(sys.argv[1]),False,int(sys.argv[3]),int(sys.argv[4]))
else:
    print('arg not recognized')
#print(set1Test)
out = pd.Series(set1Test)
out.plot()
input('Press ENTER to exit')
