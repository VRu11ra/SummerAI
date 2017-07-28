import pandas as pd
import pylab as pl
import numpy as np
import sys

def main():
    df = pd.read_csv(str(sys.argv[1]))
    b, c = np.hsplit(df,2)
    I = [b, c]
    b, c = (np.asarray(v).flatten() for v in I)
    d = pd.Series(c)
    pl.plot(b,c)
    pl.show()
#    print(np.asarray(df).reshape(df.shape[1],df.shape[0])[0].shape)
#    pd.Series(np.asarray(df).reshape(df.shape[1],df.shape[0])).plot()
#    print(pd.Series(np.asarray(df).reshape(df.shape[1],df.shape[0])[0]))
#    a = pd.Series(np.asarray(df).reshape(df.shape[1],df.shape[0])[0])
#    print(a)
#    return
main()
input('enter')
