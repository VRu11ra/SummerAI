import numpy as np
import random
import pandas as pd
import sys

print(sys.argv)

#manage data import 
#Data = pa.read_csv('file.csv').as_matrix()
#print(Data)

#define interaction
class DataSet:
  data = np.array([[],[]]) #[time],[amp]
  time = 0
  def __init__(self,amps):
    time = amps.shape
    data = np.array([[np.arange(1,time)],amps])

#random data generation
def func(size, hard, maxInterference,period, low, high):
  iter = 0
  out = np.zeros(size-1)
  for i in a:
    if(high>= iter&& iter >=low):
      out[iter] = np.sin(i*(2*np.pi)/period)
    else:
      out[iter] = 0
    if (hard != True):
      for alpha in np.random.rand(maxInterference):
        out[iter] += random.random()*np.sin(((i*np.pi*2)/period)+alpha) #generate interference
    iter +=1
  return out

set1Test = func(1000, False, 2, 90)
#if(sys.argv[2] == 'y'):
#    set1Test = func(int(sys.argv[1]),True,int(sys.argv[3]),int(sys.argv[4]))
#elif(sys.argv[2] == 'n'):
#    set1Test = func(int(sys.argv[1]),False,int(sys.argv[3]),int(sys.argv[4]))
#else:
#    print('arg not recognized')
print(set1Test)
out = pd.Series(set1Test)
out.plot()

input('Press ENTER to exit')
