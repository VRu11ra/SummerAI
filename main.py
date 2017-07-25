import numpy as np
import random
import pandas as pd
import sys
import pylab as pl
'''
How to call:
    python main.py size hard(y/n) interference period low high 
size: sample number of points to plot
hard: gen interference? --- boolean ??
interference: how much to garble signal 
period: how many cycles to display -- user input 
interference appears to work counterintuitively, where as interference value increases, the actual variance decreases. This isn't an immediate issue and can be ignored. 

'''

interference = 0
period = 0
size = 0

# class DataSet:
#   data = np.array([[],[]]) #[time],[amp]
#   time = 0
#   def __init__(self,amps):
#     time = amps.shape
#     data = np.array([[np.arange(1,time)],amps])

#random data generation, generates amplitudes
def func(size, hard, maxInterference,period, low, high):
  a = np.arange(1,size)
  iter = 0
  out = np.zeros(size-1)
  for i in a:		
      if(high>= iter and iter >=low):		
        out[iter] = np.sin(i*(2*np.pi)/period)		
      else:		
        out[iter] = 0
      if (hard != True):
          for alpha in np.random.rand(maxInterference):
              out[iter] += random.random()*np.sin(((i*np.pi*2)/period)+alpha) #generate interference
      iter +=1
  return np.asarray(out)


#print(func(200,True,3,2))

#cli interface
if(sys.argv[2] == 'y'):
    set1Test = func(int(sys.argv[1]),True,int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]), int(sys.argv[6]))
elif(sys.argv[2] == 'n'):
    set1Test = func(int(sys.argv[1]),False,int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]), int(sys.argv[6]))
else:
    print('arg not recognized')


print(type(set1Test))
# This makes a plot
out = pd.Series(set1Test)
pl.plot(out)
pl.show()
input('Press ENTER to exit')
